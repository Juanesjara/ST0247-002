import numpy as np


def levenshtein(A : str, B : str) -> int:
  return levenshteinAux(A,B,0,0) 


def levenshteinAux(A, B, i, j) -> int:
  if i == len(A) or j == len(B):
    return 0
  elif A[i] == B[j]:
    return  levenshteinAux(A,B,i+1,j+1)
  else:
    return 1 + min( levenshteinAux(A,B,i+1,j), levenshteinAux(A,B,i,j+1), levenshteinAux(A,B,i+1,j+1))


def main():
  print(" --- RECURSION ---")
  print(levenshtein("abdace","babce"))
  print(levenshtein("benyam","ephrem"))
  print(levenshtein("casita","mamita"))
main()

