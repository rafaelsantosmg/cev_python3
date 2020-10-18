"""Faça um programa que leia um número inteiro na tela e mostre sua tabuada."""

from utilidadescev.dado import leiaint
from utilidadescev.string import linha, cabeçalho

linha(45, 'verde')
n = leiaint('Digite um número para mostrar sua tabuada: ')
linha(45, 'verde')
cabeçalho(f' TABUADA DO {n} ', 20, 'azul', '=', '-')
linha(14, 'vermelho')
print(f' {n} x  1 = {n * 1}')
print(f' {n} x  2 = {n * 2}')
print(f' {n} x  3 = {n * 3}')
print(f' {n} x  4 = {n * 4}')
print(f' {n} x  5 = {n * 5}')
print(f' {n} x  6 = {n * 6}')
print(f' {n} x  7 = {n * 7}')
print(f' {n} x  8 = {n * 8}')
print(f' {n} x  9 = {n * 9}')
print(f' {n} x 10 = {n * 10}')
linha(14, 'vermelho')
