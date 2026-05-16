{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMUnVTyvprYG9uG3FkIw0qL",
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
        "<a href=\"https://colab.research.google.com/github/18mahi/ai-ml-learning-journey/blob/main/Student_Grade_analyzer.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "_M7lsg1g-S2c",
        "outputId": "76218db6-16e0-4322-c824-7d97ae2746ec"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter student name : Mahi\n"
          ]
        }
      ],
      "source": [
        "#Ask for student name\n",
        "\n",
        "stu=input(\"Enter student name : \")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# ask for marks in 5 subjects\n",
        "total_marks = 0\n",
        "has_failed_subject = False\n",
        "for i in range(1,6):\n",
        "  mark_input = input(f\"Enter marks for Subject {i}: \")\n",
        "  total_marks = total_marks + int(mark_input)\n",
        "  if(int((mark_input)))<33:\n",
        "    has_failed_subject = True"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "hx2xtOVR_Lpw",
        "outputId": "95b7189c-471a-4277-fe56-e314221c873e"
      },
      "execution_count": 33,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter marks for Subject 1: 98\n",
            "Enter marks for Subject 2: 65\n",
            "Enter marks for Subject 3: 21\n",
            "Enter marks for Subject 4: 64\n",
            "Enter marks for Subject 5: 32\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "## percentage\n",
        "percentage = (total_marks / 500) * 100\n",
        "\n",
        "##grade\n",
        "\n",
        "if(percentage>=90):\n",
        "  Grade= \"A+\"\n",
        "elif(percentage>=80 and percentage<=89):\n",
        "  Grade= \"A\"\n",
        "elif(percentage>=70 and percentage<=79):\n",
        "  Grade= \"B\"\n",
        "elif(percentage>=60 and percentage<=69):\n",
        "  Grade= \"C\"\n",
        "elif(percentage>=50 and percentage<=59):\n",
        "  Grade=\"D\"\n",
        "else:\n",
        "  Grade= \"F\""
      ],
      "metadata": {
        "id": "UGfZyfRzAKW1"
      },
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# pass rule\n",
        "if(percentage>=40 and has_failed_subject == False):\n",
        "    Status=\"Pass\"\n",
        "else:\n",
        "  Status=\"Fail\""
      ],
      "metadata": {
        "id": "eNfTtVAoa3us"
      },
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# final report\n",
        "\n",
        "print(\"\\n------ Student Grade Report ------\")\n",
        "print(f\"Name: {stu}\")\n",
        "print(f\"Total Marks: {total_marks}/500\")\n",
        "print(f\"Percentage: {percentage:.2f}%\")\n",
        "print(f\"Grade: {Grade}\")\n",
        "print(f\"Status: {Status}\")\n",
        "print(\"----------------------------------\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "oNfIKdood66C",
        "outputId": "b56002d4-8fd6-44c4-df3a-9a7111b5b742"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "------ Student Grade Report ------\n",
            "Name: Mahi\n",
            "Total Marks: 280/500\n",
            "Percentage: 56.00%\n",
            "Grade: D\n",
            "Status: Fail\n",
            "----------------------------------\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#bonus task\n",
        "import statistics as math\n",
        "marks=[]\n",
        "for i in range(1,6):\n",
        "  marks.append(int(input(f\"enter marks of subject {i}: \")))\n",
        "print(\"highest marks: \",max(marks))\n",
        "print(\"lowest marks: \",min(marks))\n",
        "print(\"average marks: \",math.mean(marks))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "-cnQd5hsgB0P",
        "outputId": "2a02de91-87ac-45d4-af1a-411c0458198e"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter marks of subject 1: 65\n",
            "enter marks of subject 2: 62\n",
            "enter marks of subject 3: 54\n",
            "enter marks of subject 4: 21\n",
            "enter marks of subject 5: 87\n",
            "highest marks:  87\n",
            "lowest marks:  21\n",
            "average marks:  57.8\n"
          ]
        }
      ]
    }
  ]
}