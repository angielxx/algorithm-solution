function solution(nodeinfo) {
    const p = Array.from({length:nodeinfo.length}, _ => null);
    const l = Array.from({length:nodeinfo.length}, _ => null);
    const r = Array.from({length:nodeinfo.length}, _ => null);
    
    // 왼쪽트리, 오른쪽트리로 나눔 -> 그 안에서 루트 찾고 왼쪽트리, 오른쪽트리 나눔 -> ...
    function getTree(nodes) {
        if (!nodes.length) return null;
        
        nodes.sort((a, b) => nodeinfo[b][1] - nodeinfo[a][1]);
        const root = nodes[0];
        const root_x = nodeinfo[root][0];
        const temp = nodes.slice(1);
        const leftTree = [];
        const rightTree = [];
        
        for (let i = 0; i < temp.length; i++) {
            const n = temp[i];
            if (nodeinfo[n][0] < root_x) leftTree.push(n);
            else rightTree.push(n);
        }

        const leftRoot = getTree(leftTree);
        const rightRoot = getTree(rightTree);

        if (leftRoot !== null) {
            l[root] = leftRoot;
            p[leftRoot] = root;
        }
        if (rightRoot !== null) {
            r[root] = rightRoot;
            p[rightRoot] = root;
       }
        
        return root
    }
    
    const nodes = Array.from({length:nodeinfo.length}, (_, i) => i);
    const root = getTree(nodes);
    
    return [preorder(p,l,r,root), postorder(p,l,r,root)]
}

function preorder(p, l, r, root) {
    const result = [];
    
    function _preorder(root) {
        result.push(root + 1);
        if (l[root] !== null) {
            _preorder(l[root]);
        }
        if (r[root] !== null) {
            _preorder(r[root]);
        }
    }
    _preorder(root);
    
    return result;
}

function postorder(p, l, r, root) {
    const result = [];
    
    function _postorder(root) {
        if (l[root] !== null) {
            _postorder(l[root]);
        }
        if (r[root] !== null) {
            _postorder(r[root]);
        }
        result.push(root + 1)
    }
    _postorder(root);
    
    return result
}