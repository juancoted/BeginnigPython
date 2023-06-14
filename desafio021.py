print('===== DESAFIO 018 =====')
print('Faça um programa em python que abra e reproduza um áudio de um arquivo em MP3')
import pygame

#pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('nerdcast_880_sempauta.mp3')
pygame.mixer.music.play()

pygame.event.wait()
