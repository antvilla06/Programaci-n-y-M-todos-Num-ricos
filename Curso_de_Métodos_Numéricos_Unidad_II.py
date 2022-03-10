{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/antvilla06/Programaci-n-y-M-todos-Num-ricos/blob/main/Curso_de_M%C3%A9todos_Num%C3%A9ricos_Unidad_II.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jLMrHy4rC-Lh"
      },
      "source": [
        "\n",
        "\n",
        "```\n",
        "# Esto tiene formato de código\n",
        "```\n",
        "\n",
        "# Recurrencias"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "CfCcSjK5OcTr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "x9J7OXJADBRW"
      },
      "source": [
        "\n",
        "\n",
        "```\n",
        "# Esto tiene formato de código\n",
        "```\n",
        "Una recurrencia es un proceso repetido con los números naturales\n",
        "\n",
        "Ejemplos:\n",
        "\n",
        "Escribir los npuneros naturales del 0 al 10.\n",
        "\n",
        "Paso 1:  $n = 0$\n",
        "\n",
        "Paso 2: \n",
        "\n",
        "  $ 1 = 0+1$\n",
        "\n",
        "  $ 2 = 1 + 1$\n",
        "\n",
        "  $ 3 = 2 + 1$\n",
        "\n",
        "  ...\n",
        "\n",
        "  $8=7+1$\n",
        "\n",
        "  $9=8+1$\n",
        "\n",
        "  $10=9+1$\n",
        "\n",
        "Se escribe como\n",
        "  $n = n +1$ \n",
        "\n",
        "\n",
        "\n",
        " \n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "roAfgs2rGI1w",
        "outputId": "e8191c36-b7f5-4224-80c3-65fe2b8f276a"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n"
          ]
        }
      ],
      "source": [
        "n = 0\n",
        "\n",
        "n = n+1\n",
        "print(n)\n",
        "#Hasta aqui el valor de n = 1\n",
        "n = n +1\n",
        "print(n)\n",
        "#Hasta aqui el valor de n = 2\n",
        "n = n +1\n",
        "print(n)\n",
        "#Hasta aqui el valor de n = 3\n",
        "n = n +1\n",
        "print(n)\n",
        "#Hasta aqui el valor de n = 4\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7rBytP_rMpCG"
      },
      "source": [
        "Sucesión de núeros impares.\n",
        "\n",
        "0° impar es  1=2*0+1\n",
        "\n",
        "1° impar es  3=2*1+1\n",
        "\n",
        "2° impar es  5=2*2+1\n",
        "\n",
        "3° impar es  7=2*3+1\n",
        "\n",
        "4° impar es  9=2*4+1 \n",
        "\n",
        "\n",
        "Si quiero saber el número impar con pisicón=35\n",
        "  2*35+1=71\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IymF92QVOYKj",
        "outputId": "4b7588a3-6494-4710-d630-76fbeeccfb43"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "1\n",
            "3\n",
            "5\n",
            "7\n",
            "9\n"
          ]
        }
      ],
      "source": [
        "#El número n es la posición\n",
        "#Formula de número impar impar=2*n+1\n",
        "\n",
        "n=0\n",
        "impar = 2*n+1\n",
        "print(impar)\n",
        "#La posición es n =0\n",
        "\n",
        "n = n+1\n",
        "impar = 2*n +1 \n",
        "print(impar)\n",
        "#La posición es n =1\n",
        "\n",
        "n = n+1  #3 = 2+1\n",
        "impar = 2*n +1 \n",
        "print(impar)\n",
        "#La posición es n =2\n",
        "\n",
        "n = n+1  #3 = 2+1\n",
        "impar = 2*n +1 \n",
        "print(impar)\n",
        "#La posición es n =3\n",
        "\n",
        "n = n+1  #4 = 3+1\n",
        "impar = 2*n +1 \n",
        "print(impar)\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "j4fRY1dczrn4"
      },
      "source": [
        "Hacer una lista de números pares. Los números pares son de la forma $2n$ donde $n$ es un número natural.\n",
        "\n",
        "1. n = 0 definir par=2*n.\n",
        "\n",
        "2.  n = 1 definir par = 2*n\n",
        "\n",
        "3. n = 2 definir par= 2*n\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tsyfz82V1VPZ",
        "outputId": "a477fb9a-fd58-499a-ea8e-0b8f6aae628d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "0\n",
            "2\n",
            "4\n",
            "6\n",
            "8\n",
            "10\n",
            "12\n"
          ]
        }
      ],
      "source": [
        "# Construir los números paressegpun su pisición.\n",
        "#La forma de los npumeros pares es par = 2*n.\n",
        "\n",
        "n=0\n",
        "par = 2*n\n",
        "print(par)\n",
        "\n",
        "n = n+1 #El nuevo valor de n == 0+1 ==1\n",
        "par = 2*n\n",
        "print(par)\n",
        "\n",
        "n=n+1 #El nuevo valor de n == 1+1==2\n",
        "par= 2*n\n",
        "print(par)\n",
        "\n",
        "n=n+1 #El nuevo valor de n == 2+1==3\n",
        "par= 2*n\n",
        "print(par)\n",
        "\n",
        "n=n+1 #El nuevo valor de n == 3+1==4\n",
        "par= 2*n\n",
        "print(par)\n",
        "\n",
        "n=n+1 #El nuevo valor de n == 4+1==5\n",
        "par= 2*n\n",
        "print(par)\n",
        "\n",
        "n=n+1 #El nuevo valor de n == 5+1==6\n",
        "par= 2*n\n",
        "print(par)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kpBNdxIo4Wn3"
      },
      "source": [
        "Fracciones con numrador impar y numerador par.\n",
        "\n",
        "$\\frac{5}{8}$, $\\frac{7}{100}$ \n",
        "\n",
        "1. n = 0. frac=$\\frac{2n+1}{2n}$\n",
        "\n",
        "2. n = n+1   frac=$\\frac{2n+1}{2n}$.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 224
        },
        "id": "1l9XtEiy5x2-",
        "outputId": "3efeacf3-f7c9-4594-a440-e26410e35ed3"
      },
      "outputs": [
        {
          "ename": "ZeroDivisionError",
          "evalue": "ignored",
          "output_type": "error",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-7-20db229609e3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mn\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0mfrac\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mn\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m/\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mn\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfrac\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mZeroDivisionError\u001b[0m: division by zero"
          ]
        }
      ],
      "source": [
        "#Hacr fracciones con numerador impar y denominador par.\n",
        "\n",
        "n=0\n",
        "frac = (2*n+1)/(2*n)\n",
        "print(frac)\n",
        "\n",
        "#Hay error por divir entre cero."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BiAFxLwW7K3A",
        "outputId": "88187385-bdbf-40b7-ab02-3b4c75ceed6a"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "1.5\n",
            "1.25\n",
            "1.1666666666666667\n"
          ]
        }
      ],
      "source": [
        "\n",
        "\n",
        "n=1\n",
        "frac = (2*n+1)/(2*n)\n",
        "print(frac)\n",
        "\n",
        "n=n+1\n",
        "frac = (2*n+1)/(2*n)\n",
        "print(frac)\n",
        "\n",
        "n=n+1\n",
        "frac = (2*n+1)/(2*n)\n",
        "print(frac)\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yODRqVKF8bFh"
      },
      "source": [
        "Hacer una sequencia números impares elevados al cuadrado.\n",
        "\n",
        "5**2\n",
        "\n",
        "print(impar)\n",
        "print(impar**2)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UEXO3KfjDt2Q"
      },
      "source": [
        "Condicionales if else.\n",
        "\n",
        "1. Si clase es antes de las 8 no voy al tec.\n",
        "\n",
        "2. De otra forma si voy.\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TOTa7p8HEmeB",
        "outputId": "e258cad3-914e-4ac6-8b40-fd46adc4ec92"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Si voy al tec\n"
          ]
        }
      ],
      "source": [
        "clase = 8 \n",
        "\n",
        "if clase < 8: \n",
        "  print(\"No voy al tec\")\n",
        "else:\n",
        "  print(\"Si voy al tec\")  \n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GWmhaQbgGEiF"
      },
      "source": [
        "\n",
        "1.Si el kilo de limon cuesta menos de 70 compro 5 kilos.\n",
        "\n",
        "2. De otra forma compro 2"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ee1spkzYGUYF",
        "outputId": "21d64b1f-a0e3-4888-e0c1-3dc34389af1d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "140\n"
          ]
        }
      ],
      "source": [
        "kilo_limon = 70\n",
        "\n",
        "if kilo_limon < 70:\n",
        "  gasto = 5*kilo_limon\n",
        "  print(gasto)\n",
        "  \n",
        "else:\n",
        "  gasto = 2*kilo_limon\n",
        "  print(gasto)\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rIyNCpRZHzww"
      },
      "source": [
        "Si juegas con un amigo con un dado \n",
        "\n",
        "1. Si sale numero par ganas 10 pesos.\n",
        "2. si sale impar pierdes 20.\n",
        "\n",
        "\n",
        "Recordatorio. Si el residuo de una división entre 2 es  0  el numero es par y si no es impar."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ke6OAONMIRaU",
        "outputId": "085da335-23cb-4c8f-8680-7570783bf7bf"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "1"
            ]
          },
          "execution_count": 13,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "6%2\n",
        "\n",
        "7%2\n",
        "\n",
        "10001%2\n",
        "\n",
        "9%4"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Qa3CI5E1JV-Y",
        "outputId": "ce074571-513b-43ca-bb7b-fbd5c23ecddb"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Pierdes 20 pesos\n"
          ]
        }
      ],
      "source": [
        "dado = -11\n",
        "\n",
        "if dado%2==0:\n",
        "  print(\"Ganas 10 pesos\")\n",
        "else:\n",
        "  print(\"Pierdes 20 pesos\")\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5lpchJ_BKW5y"
      },
      "source": [
        "Si hay mas condicionales usamos elif\n",
        "\n",
        "1. Si el kilo de limon cuesta menos de 70 compro 5 kilos.\n",
        "\n",
        "2. Si Cuesta entre 70 y 80 pesos compro 3.\n",
        "\n",
        "3. De otra forma compro 2\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "snMURet3MGTX",
        "outputId": "8b137f21-8bd4-4082-e27b-d9c381b66115"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "160\n"
          ]
        }
      ],
      "source": [
        "\n",
        "kilo_limon = 80\n",
        "\n",
        "if kilo_limon<70:\n",
        "  gasto = 5*kilo_limon\n",
        "  print(gasto)\n",
        "\n",
        "elif kilo_limon <80:\n",
        "  gasto = 4*kilo_limon\n",
        "  print(gasto)\n",
        "\n",
        "else:\n",
        "  gasto = 2*kilo_limon\n",
        "  print(gasto)  \n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "O-UiKNsSODsp"
      },
      "source": [
        "Algoritmo  de Collatz \n",
        "\n",
        "Tomar un número.\n",
        "\n",
        "1. Si el número es par se divide entre 2.\n",
        "\n",
        "2. Si es impar se multiplica por 3 y se suma 1."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kb-FdG17Oj01",
        "outputId": "9a7c83ba-215c-4596-a32f-79f08ff2dcb3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "5.0\n"
          ]
        }
      ],
      "source": [
        "numero = 10\n",
        "\n",
        "if numero % 2==0:\n",
        "    print(numero/2)\n",
        "\n",
        "else: \n",
        "  print(3*numero +1 )    \n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "v7MT682MRZIE"
      },
      "source": [
        "\n",
        "\n",
        "1. Agrupar a los alumnos con calificación aprobatoria 6.\n",
        "\n",
        "    a.   No hacen examen los que tienen calificación myor o igual a 9.\n",
        "\n",
        "    b.   Si hacen exmen los demas.\n",
        "\n",
        "\n",
        "2. Calificación reprobdo.\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FO1jE9RcTGv6",
        "outputId": "4d07af4f-b06c-440a-9746-34ee81c121d7"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "No haces examen\n"
          ]
        }
      ],
      "source": [
        "\n",
        "cal = 9\n",
        "\n",
        "if cal >= 6:\n",
        "    if cal >= 9:                        #Esta seccion toma en cuenta cal >= 6.\n",
        "      print(\"No haces examen\")\n",
        "    else:\n",
        "      print(\"Si haces examen\")\n",
        "\n",
        "    \n",
        "\n",
        "\n",
        "else:\n",
        "  print(\"reprobado el semestre\")  \n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "asw4WzKqVi_4"
      },
      "source": [
        "\n",
        "Tomar un número.\n",
        "\n",
        "\n",
        "1. Si el numero es par\n",
        "        a. Si es mayor a 20 restarle el mismo número.\n",
        "        b. Menor que 20 duplicarlo.\n",
        "\n",
        "2. De otra forma no hacer nada.        "
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "```\n",
        "\n",
        "```\n",
        "\n",
        "# Loops \"While\".\n"
      ],
      "metadata": {
        "id": "Y8icXKAtUXiA"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Conjetura de Collatz"
      ],
      "metadata": {
        "id": "44ZLX9B_eMNO"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "mEdiffmmvaxW"
      },
      "outputs": [],
      "source": [
        "\n",
        "def collatz(n):\n",
        "  A=[]\n",
        "  while n!=1:\n",
        "    if n%2==0:\n",
        "     n = int(n/2)\n",
        "    else:\n",
        "     n = 3*n+1\n",
        "    A.append(n)\n",
        "    m = len(A)\n",
        "    print(n)  \n",
        "\n",
        "  print(m)     "
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "collatz(27)"
      ],
      "metadata": {
        "id": "LzewrfwPxsc9",
        "outputId": "718311ad-f8e3-4380-f4a8-5517c0c56034",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "82\n",
            "41\n",
            "124\n",
            "62\n",
            "31\n",
            "94\n",
            "47\n",
            "142\n",
            "71\n",
            "214\n",
            "107\n",
            "322\n",
            "161\n",
            "484\n",
            "242\n",
            "121\n",
            "364\n",
            "182\n",
            "91\n",
            "274\n",
            "137\n",
            "412\n",
            "206\n",
            "103\n",
            "310\n",
            "155\n",
            "466\n",
            "233\n",
            "700\n",
            "350\n",
            "175\n",
            "526\n",
            "263\n",
            "790\n",
            "395\n",
            "1186\n",
            "593\n",
            "1780\n",
            "890\n",
            "445\n",
            "1336\n",
            "668\n",
            "334\n",
            "167\n",
            "502\n",
            "251\n",
            "754\n",
            "377\n",
            "1132\n",
            "566\n",
            "283\n",
            "850\n",
            "425\n",
            "1276\n",
            "638\n",
            "319\n",
            "958\n",
            "479\n",
            "1438\n",
            "719\n",
            "2158\n",
            "1079\n",
            "3238\n",
            "1619\n",
            "4858\n",
            "2429\n",
            "7288\n",
            "3644\n",
            "1822\n",
            "911\n",
            "2734\n",
            "1367\n",
            "4102\n",
            "2051\n",
            "6154\n",
            "3077\n",
            "9232\n",
            "4616\n",
            "2308\n",
            "1154\n",
            "577\n",
            "1732\n",
            "866\n",
            "433\n",
            "1300\n",
            "650\n",
            "325\n",
            "976\n",
            "488\n",
            "244\n",
            "122\n",
            "61\n",
            "184\n",
            "92\n",
            "46\n",
            "23\n",
            "70\n",
            "35\n",
            "106\n",
            "53\n",
            "160\n",
            "80\n",
            "40\n",
            "20\n",
            "10\n",
            "5\n",
            "16\n",
            "8\n",
            "4\n",
            "2\n",
            "1\n",
            "111\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = 0\n",
        "m = 0\n",
        "suma=[]\n",
        "while n <7:\n",
        "  n=n+1\n",
        "  m = m+n\n",
        "  suma.append(m)\n",
        "print(suma)   \n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8fXMWuW4Oe2G",
        "outputId": "f06779ce-c418-4c66-92a3-18c99154a4c4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 3, 6, 10, 15, 21, 28]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = 0\n",
        "m = 0\n",
        "suma=[]\n",
        "for n in range(0,7):\n",
        "  n=n+1\n",
        "  m = m+n\n",
        "  suma.append(m)\n",
        "print(suma) "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3N7poUodRAQ_",
        "outputId": "ccc9030c-228f-4f69-dbea-c0eb7dd81af8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 3, 6, 10, 15, 21, 28]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = 27\n",
        "\n",
        "for k in range(0,8):\n",
        "  if n%2==0:\n",
        "    n=n/2\n",
        "  else:\n",
        "    n=3*n+1\n",
        "  #print(k)\n",
        "  print(n)  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zFyY-uuHRKh0",
        "outputId": "3cf55483-1bb3-4e62-d63b-b8b7e818e3bd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "82\n",
            "41.0\n",
            "124.0\n",
            "62.0\n",
            "31.0\n",
            "94.0\n",
            "47.0\n",
            "142.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = 27\n",
        "pasos =[]\n",
        "while n!=1:\n",
        "  if n%2==0:\n",
        "    n=n/2\n",
        "  else:\n",
        "    n=3*n+1\n",
        "    pasos.append(n)\n",
        "print(pasos)    \n",
        "len(pasos)  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Nnl_5Tl6Tj6r",
        "outputId": "edc1322e-0bce-4eef-f3a0-fe7211b5f821"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[82, 124.0, 94.0, 142.0, 214.0, 322.0, 484.0, 364.0, 274.0, 412.0, 310.0, 466.0, 700.0, 526.0, 790.0, 1186.0, 1780.0, 1336.0, 502.0, 754.0, 1132.0, 850.0, 1276.0, 958.0, 1438.0, 2158.0, 3238.0, 4858.0, 7288.0, 2734.0, 4102.0, 6154.0, 9232.0, 1732.0, 1300.0, 976.0, 184.0, 70.0, 106.0, 160.0, 16.0]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "41"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "IX1t7f7oVign"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "m = 1\n",
        "suma=[]\n",
        "for n in range(0,18):\n",
        "  n=n+1\n",
        "  m = m+2**(-n)\n",
        "  suma.append(m)\n",
        "print(suma)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MR2QU3zYVvxA",
        "outputId": "8277793f-e804-4f79-cf1d-c0f6dfa3a3be"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1.5, 1.75, 1.875, 1.9375, 1.96875, 1.984375, 1.9921875, 1.99609375, 1.998046875, 1.9990234375, 1.99951171875, 1.999755859375, 1.9998779296875, 1.99993896484375, 1.999969482421875, 1.9999847412109375, 1.9999923706054688, 1.9999961853027344]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "```\n",
        "# Esto tiene formato de código\n",
        "```\n",
        "\n",
        "# Funciones "
      ],
      "metadata": {
        "id": "QM2q4Kx4DUvE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def suma(x):\n",
        "  s = x +4\n",
        "  return s"
      ],
      "metadata": {
        "id": "clyYL0sdIZjW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "suma(7)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sjUIXzbsI-zM",
        "outputId": "a6d4efcd-ee21-47bd-fc64-4c5ccf4acfeb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "11"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def cuadrado(num):\n",
        "  s = num**2\n",
        "  return s"
      ],
      "metadata": {
        "id": "tGvfdOdkJQPa"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def suma_num(a,b):\n",
        "  s = a +b\n",
        "  return s "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xZ7S4vHoJqHi",
        "outputId": "5f676f7d-c9ce-4941-fdfd-f605db992451"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "49"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "E1k3TYxBLjyb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Algoritmo de Eculides"
      ],
      "metadata": {
        "id": "FPDYKVPhdt90"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def euclid_mcd(a,b):\n",
        "  \n",
        "\n",
        "  if a>b:\n",
        "    True\n",
        "  elif a<b:\n",
        "    b = a\n",
        "    a = b\n",
        "  else:\n",
        "    True    \n",
        "\n",
        "  r = 1\n",
        "\n",
        "  while r!=0: \n",
        "    q = int(a/b)\n",
        "    r = a-b*q\n",
        "    a = b\n",
        "    b = r\n",
        "    print(r)\n",
        "    \n",
        "\n",
        "  return r  \n"
      ],
      "metadata": {
        "id": "WRaMVP_tdsfl"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "```\n",
        "# Esto tiene formato de código\n",
        "```\n",
        "\n",
        "# Matrices y vectores."
      ],
      "metadata": {
        "id": "I2pcqR_WW6LI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "dztSim_hI9YW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "MZO6fZuOI96R"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "\n",
        "n = 5\n",
        "i =0\n",
        "j =0\n",
        "A =[]\n",
        "Z =[]\n",
        "\n",
        "while i <n:\n",
        "  while j < n:\n",
        "      Z.append(0)\n",
        "      j = j+1\n",
        "  A.append(Z)\n",
        "  i = i+1\n",
        "\n",
        "A =np.array(A)\n",
        "print(A)\n",
        "\n",
        "k=0\n",
        "\n",
        "while k < 4:\n",
        "  l = 0\n",
        "  while l < 4:\n",
        "    if l == k:\n",
        "      A[k][l]= 346\n",
        "    else:\n",
        "      A[k][l]=1\n",
        "    l = l+1\n",
        "  k = k+1\n",
        " \n",
        "   \n",
        "\n",
        "B = np.array(A)  \n",
        "  \n",
        "print(B)\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wbHaIE2_s0p4",
        "outputId": "b8468e70-005b-48f1-d7be-4ce05a2fba5d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[0 0 0 0 0]\n",
            " [0 0 0 0 0]\n",
            " [0 0 0 0 0]\n",
            " [0 0 0 0 0]\n",
            " [0 0 0 0 0]]\n",
            "[[346   1   1   1   0]\n",
            " [  1 346   1   1   0]\n",
            " [  1   1 346   1   0]\n",
            " [  1   1   1 346   0]\n",
            " [  0   0   0   0   0]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "\n",
        "def transpuesta(B):\n",
        "  C = B\n",
        "  A = np.array(B)\n",
        "  print(A)\n",
        "  k=0\n",
        "\n",
        "\n",
        "\n",
        "  while k < 3:\n",
        "    l = 0\n",
        "    while l < 3:\n",
        "      A[k][l]=C[l][k]\n",
        "      l = l+1\n",
        "    k = k+1\n",
        "  print(A) \n",
        "\n",
        "\n",
        "M = [[2,3,4],[5,6,7],[8,9,7]]\n",
        "transpuesta(M)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mHucodMeykG1",
        "outputId": "e680027a-ebf5-4e05-cbca-7cf64fdced7c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[2 3 4]\n",
            " [5 6 7]\n",
            " [8 9 7]]\n",
            "[[2 5 8]\n",
            " [3 6 9]\n",
            " [4 7 7]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def ceros(n):\n",
        "  i =0\n",
        "  j =0\n",
        "  A =[]\n",
        "  Z =[]\n",
        "\n",
        "  while i <n:\n",
        "    while j < n:\n",
        "      Z.append(0)\n",
        "      j = j+1\n",
        "      A.append(Z)\n",
        "    i = i+1\n",
        "\n",
        "  A =np.array(A)\n",
        "  return A\n",
        "  \n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "vaXa5TvsAlee"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "def flmatriz(n,mat):\n",
        "  matx = ceros(n)\n",
        "  D = np.array(mat)\n",
        "  long = D.shape[0]\n",
        "\n",
        "  i = 0\n",
        "  while i <len(D):\n",
        "    j = 0\n",
        "    while j < n:\n",
        "      if i+j<n:\n",
        "        matx[i+j][j] = D[i]\n",
        "      j = j+1\n",
        "    i = i+1 \n",
        "  return matx  \n",
        " \n",
        "\n",
        "\n",
        "\n",
        "mat = [1,4,6,-4,-1]    \n",
        "G = flmatriz(13,mat)\n",
        "print(G) \n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Fu3sKPr5oZmb",
        "outputId": "b0ba6afc-037a-4221-a140-9bd34fdc0f06"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[ 1  0  0  0  0  0  0  0  0  0  0  0  0]\n",
            " [ 4  1  0  0  0  0  0  0  0  0  0  0  0]\n",
            " [ 6  4  1  0  0  0  0  0  0  0  0  0  0]\n",
            " [-4  6  4  1  0  0  0  0  0  0  0  0  0]\n",
            " [-1 -4  6  4  1  0  0  0  0  0  0  0  0]\n",
            " [ 0 -1 -4  6  4  1  0  0  0  0  0  0  0]\n",
            " [ 0  0 -1 -4  6  4  1  0  0  0  0  0  0]\n",
            " [ 0  0  0 -1 -4  6  4  1  0  0  0  0  0]\n",
            " [ 0  0  0  0 -1 -4  6  4  1  0  0  0  0]\n",
            " [ 0  0  0  0  0 -1 -4  6  4  1  0  0  0]\n",
            " [ 0  0  0  0  0  0 -1 -4  6  4  1  0  0]\n",
            " [ 0  0  0  0  0  0  0 -1 -4  6  4  1  0]\n",
            " [ 0  0  0  0  0  0  0  0 -1 -4  6  4  1]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "```\n",
        "# Tiene formato de código\n",
        "```\n",
        "\n",
        "# Tarea 2"
      ],
      "metadata": {
        "id": "54V4ssttA_LR"
      }
    }
  ],
  "metadata": {
    "colab": {
      "collapsed_sections": [],
      "name": "Curso de Métodos Numéricos Unidad II.ipynb",
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyPY6Fzt0VWjU71lU+4gfrf8",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}