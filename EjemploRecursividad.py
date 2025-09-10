{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOs8GOTIrKxL0o+tcE78DCc"
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
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XXtmSRYN3Fz3",
        "outputId": "05fa3fb1-a10c-4941-8ecf-0dfa1c9e49c9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "120\n"
          ]
        }
      ],
      "source": [
        "def factorial(n):\n",
        "    if n == 0:  # Caso base\n",
        "        return 1\n",
        "    else:       # Caso recursivo\n",
        "        return n * factorial(n - 1)\n",
        "\n",
        "print(factorial(5))  # Resultado: 120"
      ]
    }
  ]
}