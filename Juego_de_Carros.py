{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Juego de Carros.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPcUmZsvQIjEczac+wN4AgD",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/CamilaVaronaB/Juego-de-Carros/blob/main/Juego_de_Carros.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SNYQ7qAvkYia",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c537b740-d77e-469f-a50f-0943816b2655"
      },
      "source": [
        "import random\n",
        "import os\n",
        "import time\n",
        "\n",
        "os.system(\"cls\")\n",
        "class Juego:\n",
        "  def __init__(self,ID):    \n",
        "    self.ID = ID     \n",
        "    print(\"Juego\", ID ,\"creado\")  \n",
        "\n",
        "class Carro:\n",
        "  def __init__(self,piloto,num):\n",
        "    self.piloto=piloto\n",
        "    self.posicion = 0\n",
        "  def __str__(self):\n",
        "    return self.piloto\n",
        "  def avanzar(self):\n",
        "    self.posicion += random.randint(1,6)*100\n",
        "\n",
        "class Pista:\n",
        "  def __init__(self,carriles, dist, guia):\n",
        "    self.carriles = carriles\n",
        "    self.dist = dist\n",
        "    self.guia = guia\n",
        "    self.pista= []\n",
        "    for i in range(carriles):\n",
        "      self.pista.append([guia]*dist)\n",
        "    print('Pista creada, con', self.carriles, 'carriles') \n",
        "\n",
        "  def ubicar_carro(self,carro,carril,posicion):\n",
        "    self.pista[carril][posicion] = carro\n",
        "  \n",
        "  def mostrar(self):\n",
        "    print(\"  SALIDA  \"+ (\"-\"*((self.dist)-4))+ \"|| META\")\n",
        "    for i in range(self.carriles):\n",
        "      print(\" \", end=\" \")\n",
        "      for j in range(self.dist):\n",
        "        print(self.pista[i][j],end=\"\")\n",
        "      print()\n",
        "\n",
        "class Jugador:\n",
        "  def __init__(self, nombre):\n",
        "    self.nombre = nombre\n",
        "  \n",
        "class Conductor(Jugador):  \n",
        "  def new(self,Ncarril,Ncarro):          \n",
        "    self.Ncarril = Ncarril\n",
        "    self.Ncarro = Ncarro\n",
        "\n",
        "os.system(\"cls\")\n",
        "\n",
        "archivo = open(\"podio.txt\",'w')\n",
        "archivo.close\n",
        "print(\"  CARRERAS DE CARROS  \")\n",
        "juego = Juego(random.randrange(1,1000))\n",
        "Jugadores = []\n",
        "#nombres = [\"maria\",\"juan\", \"carla\", \"mateo\"]\n",
        "carros= []\n",
        "print(\"Escribe a continuaci??n los nombres de los jugadores: \")\n",
        "nom = input(\"Nombre del jugador (n para no a??adir mas jugadores): \")\n",
        "while nom != 'n': \n",
        "  Jugadores.append(nom)  \n",
        "  nom = input(\"Nombre del jugador (n para no a??adir mas jugadores): \")\n",
        "\n",
        "distkm = int(input(\"Kilometros de la pista: \"))*1000\n",
        "pista = Pista(len(Jugadores),distkm,\"-\")\n",
        "\n",
        "for i in range(pista.carriles):\n",
        "  num = random.randint(1,100)\n",
        "  carro = Carro(Jugadores[i],num)\n",
        "  carros.append(carro)\n",
        "\n",
        "for i in range(pista.carriles):\n",
        "  pista.ubicar_carro(carros[i],i,carros[i].posicion) \n",
        "\n",
        "os.system(\"cls\")\n",
        "pista.mostrar()\n",
        "\n",
        "print()\n",
        "while True:\n",
        "\n",
        "  os.system(\"cls\")\n",
        "  podio = []  \n",
        "  for carro in carros:\n",
        "    if carro.posicion > pista.dist-3:\n",
        "      podio.append(carro)\n",
        "  if len(podio) > 0:\n",
        "    break\n",
        "  \n",
        "  for i in range(pista.carriles):\n",
        "    pista.ubicar_carro(pista.guia, i,carros[i].posicion)\n",
        "    carros[i].avanzar()\n",
        "    pista.ubicar_carro(carros[i],i,carros[i].posicion)\n",
        "  \n",
        "  pista.mostrar()\n",
        "  time.sleep(1)\n",
        "\n",
        "pista.mostrar()\n",
        "\n",
        "archivo = open(\"podio.txt\",'w')\n",
        "print(\"Podio\")\n",
        "for carro in podio:\n",
        "  print(\"Primer puesto\", podio[0])\n",
        "  #print(\"Segundo puesto\",podio[1])\n",
        "  #print(\"Tercer puesto\", podio[2])\n",
        "archivo.write(podio)\n",
        "archivo.close\n",
        "print()\n",
        "\n",
        "\n",
        "  "
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "  CARRERAS DE CARROS  \n",
            "Juego 803 creado\n",
            "Escribe a continuaci??n los nombres de los jugadores: \n",
            "Nombre del jugador (n para no a??adir mas jugadores): ma\n",
            "Nombre del jugador (n para no a??adir mas jugadores): mw\n",
            "Nombre del jugador (n para no a??adir mas jugadores): mi\n",
            "Nombre del jugador (n para no a??adir mas jugadores): mom\n",
            "Nombre del jugador (n para no a??adir mas jugadores): mu\n",
            "Nombre del jugador (n para no a??adir mas jugadores): n\n",
            "Kilometros de la pista: 30\n",
            "  SALIDA  -----------------------------|| META\n",
            "  ma--------------------------------\n",
            "  mw--------------------------------\n",
            "  mi--------------------------------\n",
            "  mom--------------------------------\n",
            "  mu--------------------------------\n",
            "\n",
            "  SALIDA  -----------------------------|| META\n",
            "  -ma-------------------------------\n",
            "  ---mw-----------------------------\n",
            "  -mi-------------------------------\n",
            "  -----mom---------------------------\n",
            "  -----mu---------------------------\n",
            "  SALIDA  -----------------------------|| META\n",
            "  -------ma-------------------------\n",
            "  ------mw--------------------------\n",
            "  ----mi----------------------------\n",
            "  -------mom-------------------------\n",
            "  -------mu-------------------------\n",
            "  SALIDA  -----------------------------|| META\n",
            "  ----------ma----------------------\n",
            "  ------------mw--------------------\n",
            "  ---------mi-----------------------\n",
            "  ---------mom-----------------------\n",
            "  ------------mu--------------------\n",
            "  SALIDA  -----------------------------|| META\n",
            "  -----------ma---------------------\n",
            "  -------------mw-------------------\n",
            "  ------------mi--------------------\n",
            "  -----------mom---------------------\n",
            "  --------------mu------------------\n",
            "  SALIDA  -----------------------------|| META\n",
            "  --------------ma------------------\n",
            "  ----------------mw----------------\n",
            "  ---------------mi-----------------\n",
            "  -------------mom-------------------\n",
            "  ---------------mu-----------------\n",
            "  SALIDA  -----------------------------|| META\n",
            "  ---------------ma-----------------\n",
            "  ----------------------mw----------\n",
            "  -----------------mi---------------\n",
            "  -------------------mom-------------\n",
            "  -------------------mu-------------\n",
            "  SALIDA  -----------------------------|| META\n",
            "  ---------------------ma-----------\n",
            "  -------------------------mw-------\n",
            "  ---------------------mi-----------\n",
            "  -----------------------mom---------\n",
            "  ---------------------mu-----------\n",
            "  SALIDA  -----------------------------|| META\n",
            "  ----------------------ma----------\n",
            "  ----------------------------mw----\n",
            "  -------------------------mi-------\n",
            "  -------------------------mom-------\n",
            "  ------------------------mu--------\n",
            "  SALIDA  -----------------------------|| META\n",
            "  -----------------------ma---------\n",
            "  -------------------------------mw-\n",
            "  ----------------------------mi----\n",
            "  ----------------------------mom----\n",
            "  ----------------------------mu----\n",
            "  SALIDA  -----------------------------|| META\n",
            "  -----------------------ma---------\n",
            "  -------------------------------mw-\n",
            "  ----------------------------mi----\n",
            "  ----------------------------mom----\n",
            "  ----------------------------mu----\n",
            "Podio\n",
            "Primer puesto [<__main__.Carro object at 0x7fa2441cccd0>]\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PiNHRO4oDKRT",
        "outputId": "baace5dc-79b3-4a8e-86f3-5c9f7e8166e7"
      },
      "source": [
        "print(podio[0])"
      ],
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "mw\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}