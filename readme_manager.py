#!/usr/bin/env python3
"""
LeetCode README Manager - All-in-One Solution

This single script handles all aspects of maintaining your LeetCode repository:
- Automatic README generation
- Problem counting and statistics
- Repository validation
- Synchronization checking
- File structure analysis

Usage:
    python readme_manager.py                    # Generate README (default)
    python readme_manager.py generate          # Generate README
    python readme_manager.py count             # Count problems by category
    python readme_manager.py validate          # Validate file structure
    python readme_manager.py stats             # Show detailed statistics
    python readme_manager.py check             # Check README synchronization
    python readme_manager.py help              # Show help

Features:
- Scans for LC_*.py, LC_*.java, LC_*.sql files automatically
- Generates perfectly formatted README table
- Updates progress statistics
- Validates file naming conventions
- Checks for missing solutions
- Reports synchronization status
"""

import os
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict, Counter
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple


@dataclass
class Problem:
    """Represents a LeetCode problem with its solutions."""

    number: int
    name: str
    category: str
    python_path: Optional[str] = None
    java_path: Optional[str] = None
    sql_path: Optional[str] = None
    # If a LeetCode URL is present in the top-of-file comments, prefer it
    comment_url: Optional[str] = None
    # Dynamic mapping of language name -> relative path
    solutions: Dict[str, str] = field(default_factory=dict)

    @property
    def leetcode_url(self) -> str:
        """Generate LeetCode URL from problem name."""
        url_name = self.name.lower()
        url_name = re.sub(r"[^\w\s-]", "", url_name)  # Remove special chars
        url_name = re.sub(
            r"[-\s_]+", "-", url_name
        )  # Replace spaces/hyphens/underscores
        url_name = url_name.strip("-")  # Remove leading/trailing hyphens
        return f"https://leetcode.com/problems/{url_name}/"

    @property
    def display_name(self) -> str:
        """Get display name for the problem."""
        name = self.name.replace("_", " ")
        # Handle Roman numerals and common patterns
        name = re.sub(r"\bII\b", "II", name)
        name = re.sub(r"\bI\b(?!\w)", "I", name)
        name = re.sub(r"\bIII\b", "III", name)
        return name


class LeetCodeManager:
    """Main class that handles all LeetCode repository operations."""

    # Category mapping and descriptions
    CATEGORY_INFO = {
        "binary_search": {
            "display": "Binary Search",
            "description": "Efficient searching in sorted arrays",
        },
        "bit_manipulation": {
            "display": "Bit Manipulation",
            "description": "Operations using bitwise operators",
        },
        "dynamic_programming": {
            "display": "Dynamic Programming",
            "description": "Optimization problems using memoization",
        },
        "database": {
            "display": "Database",
            "description": "SQL queries and database operations",
        },
        "greedy": {
            "display": "Greedy",
            "description": "Locally optimal choices leading to global optimum",
        },
        "hashing": {
            "display": "Hashing",
            "description": "Hash table and hash map problems",
        },
        "linkedlist": {
            "display": "Linked List",
            "description": "Single and doubly linked list operations",
        },
        "sliding_window": {
            "display": "Sliding Window",
            "description": "Subarray/substring problems",
        },
        "stack": {"display": "Stack", "description": "LIFO data structure problems"},
        "string_manipulation": {
            "display": "String Manipulation",
            "description": "String processing and algorithms",
        },
        "tree": {
            "display": "Tree",
            "description": "Binary tree traversal and manipulation",
        },
        "two_pointers": {
            "display": "Two Pointers",
            "description": "Array problems using multiple pointers",
        },
        "interview-prep": {
            "display": "Interview Prep",
            "description": "Additional problems for interview preparation",
        },
        "src": {  # Handle interview-prep/src structure
            "display": "Interview Prep",
            "description": "Additional problems for interview preparation",
        },
    }

    # Files to ignore during scanning
    IGNORE_FILES = {"listnode.py", "treeNode.py", "TreeNode.py"}

    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.problems: Dict[int, Problem] = {}

    def scan_repository(self) -> Dict[str, List[Problem]]:
        """Scan the repository for all LeetCode problems."""
        print("🔍 Scanning repository for LeetCode problems...")

        self.problems.clear()

        # Scan Python files
        self._scan_python_files()

        # Scan Java files
        self._scan_java_files()

        # Scan SQL files
        self._scan_sql_files()

        # Group problems by category
        categorized_problems = self._categorize_problems()

        print(
            f"✅ Found {len(self.problems)} unique problems across {len(categorized_problems)} categories"
        )
        return categorized_problems

    def _scan_python_files(self):
        """Scan for Python solution files."""
        python_pattern = re.compile(r"LC_(\d+)_(.+)\.py$")

        for py_file in self.base_path.rglob("LC_*.py"):
            if py_file.name in self.IGNORE_FILES:
                continue

            match = python_pattern.match(py_file.name)
            if match:
                problem_num = int(match.group(1))
                problem_name = match.group(2)
                category = py_file.parent.name

                if problem_num not in self.problems:
                    self.problems[problem_num] = Problem(
                        number=problem_num, name=problem_name, category=category
                    )

                self.problems[problem_num].python_path = str(
                    py_file.relative_to(self.base_path)
                ).replace("\\", "/")
                # Populate dynamic solutions mapping
                self.problems[problem_num].solutions["Python"] = str(
                    py_file.relative_to(self.base_path)
                ).replace("\\", "/")

                # Try to extract explicit LeetCode URL from top-of-file comments
                url = self._extract_comment_url(py_file)
                if url and not self.problems[problem_num].comment_url:
                    # Preserve the first-found in-file URL (do not overwrite)
                    self.problems[problem_num].comment_url = url

    def _scan_java_files(self):
        """Scan for Java solution files."""
        java_pattern = re.compile(r"LC_(\d+)_(.+)\.java$")

        for java_file in self.base_path.rglob("LC_*.java"):
            match = java_pattern.match(java_file.name)
            if match:
                problem_num = int(match.group(1))
                problem_name = match.group(2)

                if problem_num not in self.problems:
                    # Determine category from path
                    category = self._determine_category_from_path(java_file)
                    self.problems[problem_num] = Problem(
                        number=problem_num, name=problem_name, category=category
                    )

                self.problems[problem_num].java_path = str(
                    java_file.relative_to(self.base_path)
                ).replace("\\", "/")
                # Populate dynamic solutions mapping
                self.problems[problem_num].solutions["Java"] = str(
                    java_file.relative_to(self.base_path)
                ).replace("\\", "/")
                # Try to extract explicit LeetCode URL from top-of-file comments
                url = self._extract_comment_url(java_file)
                if url and not self.problems[problem_num].comment_url:
                    # Preserve the first-found in-file URL (do not overwrite)
                    self.problems[problem_num].comment_url = url

    def _scan_sql_files(self):
        """Scan for SQL solution files."""
        sql_pattern = re.compile(r"LC_(\d+)_(.+)\.sql$")

        for sql_file in self.base_path.rglob("LC_*.sql"):
            match = sql_pattern.match(sql_file.name)
            if match:
                problem_num = int(match.group(1))
                problem_name = match.group(2)

                if problem_num not in self.problems:
                    self.problems[problem_num] = Problem(
                        number=problem_num, name=problem_name, category="database"
                    )

                path = str(sql_file.relative_to(self.base_path)).replace("\\", "/")
                self.problems[problem_num].sql_path = path
                # Populate dynamic solutions mapping
                self.problems[problem_num].solutions["SQL"] = path
                # Try to extract explicit LeetCode URL from top-of-file comments
                url = self._extract_comment_url(sql_file)
                if url and not self.problems[problem_num].comment_url:
                    # Preserve the first-found in-file URL (do not overwrite)
                    self.problems[problem_num].comment_url = url

    def _determine_category_from_path(self, file_path: Path) -> str:
        """Determine category from file path."""
        parts = file_path.parts

        # Look for category in path parts
        for part in reversed(parts[:-1]):  # Exclude filename
            if part in self.CATEGORY_INFO:
                return part
            # Handle common variations
            if part == "src" and len(parts) > 2:
                parent = parts[-3] if parts[-2] == "src" else parts[-2]
                if parent in ["interview-prep", "interview_prep"]:
                    return "src"  # Will be mapped to Interview Prep

        # Default fallback
        return "src"

    def _extract_comment_url(self, file_path: Path) -> Optional[str]:
        """Extract the first LeetCode problem URL from the top-of-file comments.

        It reads the first N lines (default 12) and searches for a URL like
        https://leetcode.com/problems/..., supporting comment styles for
        Python (#), Java (//) and SQL (--).
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for _ in range(12):
                    line = f.readline()
                    if not line:
                        break
                    # Search for leetcode problems URL anywhere in the line
                    match = re.search(
                        r"https?://leetcode\.com/problems/[\w\-]+(?:/[\w\-]*)?", line
                    )
                    if match:
                        # Ensure we return a normalized URL (no trailing chars)
                        url = match.group(0).rstrip(". ")
                        # Guarantee it ends with a slash
                        if not url.endswith("/"):
                            url = url + "/"
                        return url
        except Exception:
            return None

    def _categorize_problems(self) -> Dict[str, List[Problem]]:
        """Group problems by category and sort them."""
        categorized = defaultdict(list)

        for problem in self.problems.values():
            categorized[problem.category].append(problem)

        # Sort problems within each category by number
        for category in categorized:
            categorized[category].sort(key=lambda p: p.number)

        return dict(categorized)

    def generate_readme(self) -> bool:
        """Generate the complete README content."""
        print("📝 Generating README content...")

        categorized_problems = self.scan_repository()

        # Calculate statistics and detect languages
        stats, languages = self._calculate_statistics(categorized_problems)

        # Generate sections
        header = self._generate_header()
        progress = self._generate_progress_section(stats)
        structure = self._generate_structure_section(categorized_problems)
        table = self._generate_problems_table(categorized_problems, languages)
        footer = self._generate_footer()

        readme_content = f"{header}\n\n{progress}\n\n{structure}\n\n{table}\n\n{footer}"

        # Write to README.md
        readme_path = self.base_path / "README.md"
        try:
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(readme_content)
            print(f"✅ README.md generated successfully!")
            print(
                f"📊 Summary: {len(self.problems)} problems across {len(categorized_problems)} categories"
            )

            # Print category breakdown
            print("\n📋 Category Breakdown:")
            for category, problems in sorted(categorized_problems.items()):
                display_name = self.CATEGORY_INFO.get(category, {}).get(
                    "display", category.title()
                )
                print(f"  - {display_name}: {len(problems)} problems")

            return True

        except Exception as e:
            print(f"❌ Error writing README.md: {e}")
            return False

    def _calculate_statistics(
        self, categorized_problems: Dict[str, List[Problem]]
    ) -> Dict[str, int]:
        """Calculate various statistics about the problems."""
        total_problems = sum(
            len(problems) for problems in categorized_problems.values()
        )
        categories_count = len(categorized_problems)

        # Detect all languages present across problems
        language_counter = Counter()
        for p in self.problems.values():
            for lang in p.solutions.keys():
                language_counter[lang] += 1

        stats = {
            "total": total_problems,
            "categories": categories_count,
        }

        # Add per-language counts to stats
        for lang, cnt in language_counter.items():
            stats[lang.lower()] = cnt

        # Return stats and ordered language list (preferred order)
        preferred = ["Java", "Python", "SQL"]
        other_langs = [l for l in sorted(language_counter.keys()) if l not in preferred]
        languages = [l for l in preferred if l in language_counter] + other_langs

        return stats, languages

    def _generate_header(self) -> str:
        """Generate the README header."""
        return """# LeetCode Problem Solving

Welcome to my LeetCode problem-solving repository! This repository contains solutions to various LeetCode problems organized by algorithm patterns and data structures, implemented in both **Python** and **Java**."""

    def _generate_progress_section(self, stats: Dict[str, int]) -> str:
        """Generate the progress tracking section."""
        # Build language lines dynamically
        lang_lines = []
        for key, value in sorted(stats.items()):
            if key in ("total", "categories"):
                continue
            # keys for languages are stored in lowercase in stats
            lang_lines.append(f"- **{key.title()} Solutions**: {value}")

        lang_text = "\n".join(lang_lines)

        return f"""## 📊 Progress Tracking

- **Total Problems Solved**: {stats['total']}
{lang_text}
- **Categories Covered**: {stats['categories']}"""

    def _generate_structure_section(
        self, categorized_problems: Dict[str, List[Problem]]
    ) -> str:
        """Generate the repository structure section."""
        structure_lines = [
            "## 📁 Repository Structure",
            "",
            "The problems are categorized into the following algorithmic patterns:",
            "",
        ]

        # Sort categories for consistent output
        sorted_categories = sorted(
            categorized_problems.keys(), key=lambda x: x.replace("-", "_")
        )

        for category in sorted_categories:
            if category in self.CATEGORY_INFO:
                display_name = self.CATEGORY_INFO[category]["display"]
                description = self.CATEGORY_INFO[category]["description"]
                structure_lines.append(f"- **{display_name}** - {description}")

        return "\n".join(structure_lines)

    def _generate_problems_table(
        self, categorized_problems: Dict[str, List[Problem]], languages: List[str]
    ) -> str:
        """Generate the problems table with fixed-width columns so pipes align.

        We compute the maximum width needed for each column across the whole
        repository and then pad every cell to that width when emitting the
        per-category tables. This keeps the '|' characters vertically aligned
        in the raw Markdown file.
        """
        # Sort categories for consistent output
        sorted_categories = sorted(
            categorized_problems.keys(), key=lambda x: x.replace("-", "_")
        )

        # We'll use reference-style links to keep inline table cells short.
        refs: Dict[str, str] = {}

        # Compute maximum widths for each column across all problems (measure visible cell text only)
        widths: Dict[str, int] = {}
        # Initialize with header names
        widths["Problem"] = len("Problem")
        widths["LeetCode"] = len("LeetCode")
        for lang in languages:
            widths[lang] = max(len(lang), 3)

        # Walk every problem to measure content lengths (use short reference labels)
        for category in sorted_categories:
            for p in categorized_problems.get(category, []):
                # Problem name length
                widths["Problem"] = max(widths["Problem"], len(p.display_name))

                # LeetCode link label length (we'll use a reference id like [LC-35][lc-35])
                lc_ref = f"lc-{p.number}"
                lc_label = f"[LC-{p.number}][{lc_ref}]"
                widths["LeetCode"] = max(widths["LeetCode"], len(lc_label))
                # record the reference target (prefer comment_url)
                url = (
                    p.comment_url if getattr(p, "comment_url", None) else p.leetcode_url
                )
                refs[lc_ref] = url

                # Language link lengths (use refs like [Java-LC-35][java-lc-35])
                for lang in languages:
                    path = p.solutions.get(lang)
                    if path:
                        # Use labels without 'LC' for language columns, e.g. [Java-35][java-35]
                        ref_id = f"{lang.lower()}-{p.number}"
                        cell_label = f"[{lang}-{p.number}][{ref_id}]"
                        refs[ref_id] = path
                    else:
                        cell_label = "-"
                    widths[lang] = max(widths[lang], len(cell_label))

        # Ensure a minimum width of 3 for visual clarity
        for k in widths:
            widths[k] = max(widths[k], 3)

        table_lines: List[str] = ["## 🔍 Complete Problems List", ""]

        for category in sorted_categories:
            if category not in categorized_problems:
                continue
            problems = categorized_problems[category]
            if not problems:
                continue

            if category in self.CATEGORY_INFO:
                display_name = self.CATEGORY_INFO[category]["display"]

                # Category heading
                table_lines.append(f"### {display_name}")
                table_lines.append("")

                # Header row with padded column names
                header_cells = [
                    f"{ 'Problem'.ljust(widths['Problem']) }",
                    f"{ 'LeetCode'.ljust(widths['LeetCode']) }",
                ]
                for lang in languages:
                    header_cells.append(f"{ lang.ljust(widths[lang]) }")

                table_lines.append("| " + " | ".join(header_cells) + " |")

                # Separator row (dashes matching column widths)
                sep_cells = [
                    "-" * widths["Problem"],
                    "-" * widths["LeetCode"],
                ]
                for lang in languages:
                    sep_cells.append("-" * widths[lang])

                table_lines.append("| " + " | ".join(sep_cells) + " |")

                # Rows
                for problem in problems:
                    table_lines.append(
                        self._format_problem_row(problem, languages, widths, refs)
                    )

                table_lines.append("")

        # After tables, append reference definitions so inline cells stay short
        if refs:
            table_lines.append("")
            table_lines.append(
                "<!-- Reference-style links used below to keep tables narrow -->"
            )
            table_lines.append("")

            # Stable order: sort by numeric problem id then by ref id
            def ref_sort_key(r):
                parts = r.split("-")
                # last part should be the number; fallback to full ref
                try:
                    num = int(parts[-1])
                except Exception:
                    num = 0
                return (num, r)

            for ref_id in sorted(refs.keys(), key=ref_sort_key):
                target = refs[ref_id]
                table_lines.append(f"[{ref_id}]: {target}")

        return "\n".join(table_lines)

    def _format_problem_row(
        self,
        problem: Problem,
        languages: List[str],
        widths: Dict[str, int],
        refs: Dict[str, str],
    ) -> str:
        """Format a single problem row using provided column widths and reference ids."""
        name = problem.display_name
        # Use reference-style label for LeetCode link
        lc_ref = f"lc-{problem.number}"
        lc_label = f"[LC-{problem.number}][{lc_ref}]"

        # Pad problem name and LC link to widths
        problem_cell = name.ljust(widths["Problem"])[: widths["Problem"]]
        leet_cell = lc_label.ljust(widths["LeetCode"])[: widths["LeetCode"]]

        lang_cells = []
        for lang in languages:
            path = problem.solutions.get(lang)
            if path:
                # label without 'LC' for language columns, ref id without 'lc'
                ref_id = f"{lang.lower()}-{problem.number}"
                cell = f"[{lang}-{problem.number}][{ref_id}]"
            else:
                cell = "-"
            lang_cells.append(cell.ljust(widths[lang])[: widths[lang]])

        return "| " + " | ".join([problem_cell, leet_cell] + lang_cells) + " |"

    def _generate_footer(self) -> str:
        """Generate the README footer."""
        return """## 🚀 Getting Started

- **Python 3.x** for running Python solutions
- **Java 8+** for running Java solutions

---

**Happy Coding! 🚀**

*README auto-generated by readme_manager.py*"""

    def count_problems(self):
        """Count problems by category."""
        categorized_problems = self.scan_repository()

        print("📊 Problem Count by Category:")
        print("=" * 50)

        total_unique = len(self.problems)

        # Display results
        for category, problems in sorted(categorized_problems.items()):
            display_name = self.CATEGORY_INFO.get(category, {}).get(
                "display", category.replace("_", " ").title()
            )
            print(f"  {display_name:<25}: {len(problems):>3} problems")

        print("-" * 50)
        print(f"  {'Total Unique Problems':<25}: {total_unique:>3}")

        # Language breakdown
        python_count = sum(1 for p in self.problems.values() if p.python_path)
        java_count = sum(1 for p in self.problems.values() if p.java_path)
        sql_count = sum(1 for p in self.problems.values() if p.sql_path)

        print(f"\n📋 Solutions by Language:")
        print("-" * 30)
        print(f"  Python: {python_count} files")
        print(f"  Java:   {java_count} files")
        print(f"  SQL:    {sql_count} files")

    def validate_structure(self):
        """Validate repository structure and file naming."""
        self.scan_repository()
        issues = []

        print("🔍 Validating repository structure...")

        # Check file naming conventions
        pattern = re.compile(r"^LC_\d+_[A-Za-z0-9_]+\.(py|java|sql)$")

        all_files = []
        all_files.extend(self.base_path.rglob("LC_*.py"))
        all_files.extend(self.base_path.rglob("LC_*.java"))
        all_files.extend(self.base_path.rglob("LC_*.sql"))

        for file_path in all_files:
            if file_path.name not in self.IGNORE_FILES and not pattern.match(
                file_path.name
            ):
                issues.append(f"❌ Invalid filename: {file_path}")

        # Check for missing pairs
        python_problems = {p.number for p in self.problems.values() if p.python_path}
        java_problems = {p.number for p in self.problems.values() if p.java_path}
        sql_problems = {p.number for p in self.problems.values() if p.sql_path}

        # Find problems with only one language (excluding SQL-only)
        only_python = python_problems - java_problems - sql_problems
        only_java = java_problems - python_problems - sql_problems

        if only_python:
            print(f"\n⚠️  Problems with only Python solutions: {sorted(only_python)}")

        if only_java:
            print(f"\n⚠️  Problems with only Java solutions: {sorted(only_java)}")

        if not issues and not only_python and not only_java:
            print(
                "✅ All files follow naming conventions and have proper language pairs!"
            )
        elif not issues:
            print("✅ All files follow naming conventions!")
        else:
            print(f"\n❌ Found {len(issues)} naming issues:")
            for issue in issues:
                print(f"  {issue}")

    def show_stats(self):
        """Show detailed repository statistics."""
        categorized_problems = self.scan_repository()

        print("📈 Repository Statistics")
        print("=" * 40)

        # Problem numbers analysis
        all_problem_numbers = set(self.problems.keys())

        if all_problem_numbers:
            print(
                f"Problem Number Range: {min(all_problem_numbers)} - {max(all_problem_numbers)}"
            )
            print(f"Total Unique Problems: {len(all_problem_numbers)}")

            # Find gaps
            full_range = set(
                range(min(all_problem_numbers), max(all_problem_numbers) + 1)
            )
            missing = sorted(full_range - all_problem_numbers)

            if missing:
                print(f"Missing Problems in Range: {len(missing)}")
                if len(missing) <= 20:
                    print(f"Missing: {missing}")
                else:
                    print(
                        f"Missing: {missing[:10]}...{missing[-10:]} (showing first and last 10)"
                    )

        # Category analysis
        print(f"\nCategories: {len(categorized_problems)}")
        for category, problems in sorted(
            categorized_problems.items(), key=lambda x: len(x[1]), reverse=True
        ):
            display_name = self.CATEGORY_INFO.get(category, {}).get(
                "display", category.replace("_", " ").title()
            )
            print(f"  {display_name:<20}: {len(problems):>3} problems")

        # Language coverage
        python_count = sum(1 for p in self.problems.values() if p.python_path)
        java_count = sum(1 for p in self.problems.values() if p.java_path)
        sql_count = sum(1 for p in self.problems.values() if p.sql_path)

        print(f"\nLanguage Coverage:")
        print(
            f"  Python Solutions: {python_count}/{len(self.problems)} ({python_count/len(self.problems)*100:.1f}%)"
        )
        print(
            f"  Java Solutions:   {java_count}/{len(self.problems)} ({java_count/len(self.problems)*100:.1f}%)"
        )
        print(
            f"  SQL Solutions:    {sql_count}/{len(self.problems)} ({sql_count/len(self.problems)*100:.1f}%)"
        )

    def check_readme_sync(self):
        """Check if README is in sync with actual files."""
        self.scan_repository()

        # Get problems from files
        file_problems = set(self.problems.keys())

        # Get problems from README
        readme_problems = set()
        readme_path = self.base_path / "README.md"

        try:
            with open(readme_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Find all LC-xxx patterns in links
                matches = re.findall(r"LC-(\d+)", content)
                readme_problems = set(int(match) for match in matches)
        except FileNotFoundError:
            print("❌ README.md not found!")
            return

        print("🔄 README Synchronization Check")
        print("=" * 40)

        # Find discrepancies
        in_files_not_readme = file_problems - readme_problems
        in_readme_not_files = readme_problems - file_problems

        if in_files_not_readme:
            print(
                f"❌ Problems in files but not in README ({len(in_files_not_readme)}):"
            )
            for num in sorted(in_files_not_readme):
                print(f"  LC-{num}")

        if in_readme_not_files:
            print(
                f"❌ Problems in README but not in files ({len(in_readme_not_files)}):"
            )
            for num in sorted(in_readme_not_files):
                print(f"  LC-{num}")

        if not in_files_not_readme and not in_readme_not_files:
            print("✅ README is in sync with files!")

        print(f"\nSummary:")
        print(f"  Problems in files: {len(file_problems)}")
        print(f"  Problems in README: {len(readme_problems)}")
        print(f"  Synchronized: {len(file_problems & readme_problems)}")

    def show_help(self):
        """Show help information."""
        help_text = """
🚀 LeetCode README Manager - All-in-One Solution

USAGE:
    python readme_manager.py [command]

COMMANDS:
    generate (default)  Generate README.md from repository files
    count              Count problems by category
    validate           Validate file naming and structure  
    stats              Show detailed repository statistics
    check              Check if README is synchronized with files
    help               Show this help message

EXAMPLES:
    python readme_manager.py              # Generate README
    python readme_manager.py count        # Count problems by category
    python readme_manager.py check        # Check synchronization status
    python readme_manager.py validate     # Validate file structure

FEATURES:
    ✅ Automatic file discovery (LC_*.py, LC_*.java, LC_*.sql)
    ✅ Perfect table formatting with proper alignment
    ✅ Automatic progress statistics calculation
    ✅ Category-based organization
    ✅ Working links to all solution files
    ✅ Repository validation and error checking
    ✅ Synchronization status monitoring

FILE NAMING REQUIREMENTS:
    Python:  LC_[NUMBER]_[ProblemName].py
    Java:    LC_[NUMBER]_[ProblemName].java  
    SQL:     LC_[NUMBER]_[ProblemName].sql

WORKFLOW:
    1. Add new solution files following naming convention
    2. Run: python readme_manager.py
    3. Done! README automatically updated

For more information, see the generated README.md file.
        """
        print(help_text)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="LeetCode README Manager - All-in-One Solution",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "command",
        nargs="?",
        default="generate",
        choices=["generate", "count", "validate", "stats", "check", "help"],
        help="Command to execute (default: generate)",
    )

    # Handle case where no arguments or help is requested
    if len(sys.argv) == 1:
        # Default to generate
        command = "generate"
    elif len(sys.argv) == 2 and sys.argv[1] in ["-h", "--help", "help"]:
        command = "help"
    else:
        args = parser.parse_args()
        command = args.command

    # Initialize manager
    manager = LeetCodeManager()

    print("🚀 LeetCode README Manager")
    print("=" * 30)

    # Execute command
    if command == "generate":
        success = manager.generate_readme()
        return 0 if success else 1

    elif command == "count":
        manager.count_problems()

    elif command == "validate":
        manager.validate_structure()

    elif command == "stats":
        manager.show_stats()

    elif command == "check":
        manager.check_readme_sync()

    elif command == "help":
        manager.show_help()

    return 0


if __name__ == "__main__":
    try:
        exit(main())
    except KeyboardInterrupt:
        print("\n\n❌ Operation cancelled by user")
        exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        exit(1)
