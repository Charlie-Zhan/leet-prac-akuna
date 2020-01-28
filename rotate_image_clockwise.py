class Solution:
    def rotate(self, matrix):
        n = len(matrix[0])
        for i in range (n // 2 + n % 2):
            for j in range(n // 2):
                temp = matrix[n - j -1][i]
                matrix[n - j -1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] =  matrix[i][j]
                matrix[i][j] = temp
        print(matrix)
if __name__ == '__main__':
    s = Solution()
    mat = [[1,2,3], [4,5,6], [7,8,9]]
    s.rotate(mat)