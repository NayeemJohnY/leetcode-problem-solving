package tree;

import java.util.LinkedList;
import java.util.Queue;

public class TreeNode {

    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    public TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    public static TreeNode buildTree(Integer... values){

        TreeNode root = new TreeNode(values[0]);
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int i =1;
        while ( i < values.length ){
            TreeNode current = queue.poll();
            if (i < values.length && values[i] != null){
                current.left = new TreeNode(values[i]);
                queue.add(current.left);
            }
            i++;

            if (i < values.length && values[i] != null){
                current.right = new TreeNode(values[i]);
                queue.add(current.right);
            }
            i++;
            
        }

        return root;
    }

}
