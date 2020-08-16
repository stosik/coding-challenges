package goldman;

import java.util.Arrays;

public class NQueen {
    public static int [][] generateBoard(int n) {
        int [][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = 0;
            }
        }
        return board;
    }

    static boolean isSafe(int[][] board, int row, int col) {
        int i, j;
        for (i = 0; i < col; i++)
            if (board[row][i] == 1)
                return false;

        for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
            if (board[i][j] == 1)
                return false;

        for (i = row, j = col; j >= 0 && i < board.length; i++, j--)
            if (board[i][j] == 1)
                return false;
        return true;
    }

    public static boolean solveNQueenUntil(int [][] board, int col) {
        if (col >= board.length) {
            return true;
        }

        for (int i = 0; i < board.length; i++) {
            if (isSafe(board, i, col)) {
                board[i][col] = 1;
                if (solveNQueenUntil(board, col + 1))
                    return true;
                board[i][col] = 0;
            }
        }
        return false;
    }


    public static void main(String[] args) {
        int N = 5;
        int[][] board = generateBoard(N);

        if(!solveNQueenUntil(board, 0)) {
            return;
        }

        System.out.println(Arrays.deepToString(board));
    }
}
