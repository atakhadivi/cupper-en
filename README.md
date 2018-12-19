# Cupper V2.0！

### Introduction

The name of Cupper means be better than common user passwords profiler (cupp). At V1.0, I made up my mind to make this tool the best social code generator in China. Until now, there is no independent tool for generating social worker passwords. After half a year, I finally completed the V2.0 version. Compared with the first version, the function of this version has been greatly improved. I will continue to update this tool in the future. I hope this tool will play a positive role in your learning and penetration testing.

### Screenshot
Version information:

![Image text](https://raw.githubusercontent.com/Saferman/cupper/master/images/version.png)

### Features

The functions that cupper can achieve are as follows:

- Generate a list of possible passwords for the target based on the information of the target (core function)
- Various processing of various password dictionaries, including checking and deleting duplicate passwords, adding new content for each line of passwords, case conversion, merging password dictionaries, analyzing password dictionaries, sorting passwords according to certain rules Improve cracking efficiency
- Download the common password dictionary provided by the author

### Highlight

In the V1.0 version, the basic prototype of the cupper is close to the social code module in the domestic pententdb, but many improvements have been made in the password generation algorithm to improve the accuracy of the target password. But with the actual use, I found a lot of shortcomings that mimic the structure of the pendesdb module.：

- First, the social worker password generation function is just a simple py script in the pendesdb, it is difficult to come up directly as a tool for the hand.
- Second, the use of cupperV1.0 is extremely inconvenient. If the amount of input user information is large, each input is tired.
- Third, even if I improved the original algorithm, the tool still can't handle very complicated situations, and the improvement of the algorithm is not scientific. The improvement of accuracy is not very big based on personal experience.

In view of these problems, I made a substantial improvement in V2.0:

- First, the algorithm is improved. This time, my opponent's cryptosystem is analyzed and extracted. A simple neural network is constructed to analyze the cryptographic structure and classify it. A threshold is set. The cryptographic structure appears more frequently than the threshold. Will be absorbed into the cupper algorithm
- Second, in order to solve the user's troubles of repeatedly inputting information for the same target, the user input is automatically saved.
- Third, this version of the tool is still based on a person-oriented social worker generator, but added a password guessing scenario for the website, and will continue to increase in the future.
- Fourth, an order is added to the file processing of the password. This tool will give each password a weight to indicate the possibility that the password will be used by the user, and then the password will be placed in order from highest to lowest according to the weight. Improve the efficiency of cracking in password files
- Fifth, other parts of the details change, such as the general weak password file from the original 10 to 33, password file analysis to get more information, etc.
- Sixth, this tool is written in pure python, and for the sake of convenience, try to use Python's own module, no extra dependencies. The previous version of the V1.0 tool is only available under Linux, this time support windows
- Seventh, the password generation algorithm is the same as V1.0, encapsulated in the PasswordGenerator object in createpassword.py, you can use this algorithm in your program by the following method:

<code>import createpassword
pg = PasswordGenerator(Target information)
password_list = pg.generator()</code>

### usage

Direct execution
<code>python cupper.py -h</code>
Note: The python version is 2.x, recommended 2.7~2.9.


### Outlook

Artificial intelligence and machine learning are used in information security. In future versions, I will add more algorithms in the field of artificial intelligence to better mine password structure rules and analyze password files, and ultimately improve the accuracy of password guessing. degree
