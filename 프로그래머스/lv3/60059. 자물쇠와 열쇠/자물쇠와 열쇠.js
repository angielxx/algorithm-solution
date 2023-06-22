function attach(x, y, M, key, board) {
  for (let i = 0; i < M; i++) {
    for (let j = 0; j < M; j++) {
      board[x + i][y + j] += key[i][j];
    }
  }
}

function detach(x, y, M, key, board) {
  for (let i = 0; i < M; i++) {
    for (let j = 0; j < M; j++) {
      board[x + i][y + j] -= key[i][j];
    }
  }
}

function rotate90(arr) {
  return arr[0].map((_, index) => arr.map(row => row[index])).reverse();
}

function check(board, M, N) {
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (board[M + i][M + j] !== 1) {
        return false;
      }
    }
  }
  return true;
}

function solution(key, lock) {
  const M = key.length;
  const N = lock.length;

  const board = Array(M * 2 + N)
    .fill(0)
    .map(() => Array(M * 2 + N).fill(0));

  // Place the lock at the center of the board
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      board[M + i][M + j] = lock[i][j];
    }
  }

  let rotatedKey = key;

  // All directions (4 loops)
  for (let _ = 0; _ < 4; _++) {
    rotatedKey = rotate90(rotatedKey);
    for (let x = 1; x < M + N; x++) {
      for (let y = 1; y < M + N; y++) {
        // Try inserting the key
        attach(x, y, M, rotatedKey, board);
        // Check if the lock is possible
        if (check(board, M, N)) {
          return true;
        }
        // Remove the key
        detach(x, y, M, rotatedKey, board);
      }
    }
  }

  return false;
}