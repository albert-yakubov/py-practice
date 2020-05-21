boolean isBalanced(TreeNode root){
//base case
if(root == null){}
    return true;
}
int heightDiff = getTreeHeight(root.left) - getTreeHeight(root.right);
if(Math.abs(heightDiff)> 1{
    return false;
}else{
    return isBalanced(root.left) && isBalanced(root.right)
}
int getTreeHeight(){
    if(node == null){
    return -1
    }
    Math.max(root.left, root.right) + 1;
}