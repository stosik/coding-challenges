import java.util.HashSet;

public class IsValidSudoku {

    public boolean (char[][] grid) {
        final HashSet<String> seen = new HashSet();
        
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                final char current_val = grid[i][j];
                if(current_val != '.') {
                    if(!seen.add(current_val + " found in a row " + i) 
                    || !seen.add(current_val + " found in a column " + j)
                    || !seen.add(current_val + " found in a sub-grid " + i/3 + "-" + j/3)
                    ) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}