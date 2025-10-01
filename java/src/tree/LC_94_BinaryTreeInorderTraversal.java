package tree;

import java.util.ArrayList;
import java.util.List;

public class LC_94_BinaryTreeInorderTraversal {
    public void traverseInorder(List<Integer> list, TreeNode node) {
        if (node != null) {
            traverseInorder(list, node.left);
            list.add(node.val);
            traverseInorder(list, node.right);
        }
    }

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        traverseInorder(list, root);
        return list;
    }

    public static void main(String[] args) {
        TreeNode root = TreeNode.buildTree(1,2,3,4,5,null,8,null,null,6,7,9);
        LC_94_BinaryTreeInorderTraversal traversel = new LC_94_BinaryTreeInorderTraversal();
        System.out.println(traversel.inorderTraversal(root));
    }

}
