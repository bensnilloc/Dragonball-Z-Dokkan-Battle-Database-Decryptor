# Dragonball Z: Dokkan Battle Database Decryptor

This tool allows you to decrypt the database from Dragonball Z: Dokkan Battle instantaneously rather than the current (known) method using <b>pysqlsimplecipher</b> which depending on your computers specs can take up to 5 minutes before a database has been decrypted.

# Requirements

<b>Windows</b><br>
<code>pip install pysqlcipher3</code><br><br>
<b>Linux/Mac OS</b><br>
<code>pip3 install pysqlcipher3</code><br><br>
In most cases, the above installation will work without an issue to install <b>pysqlcipher3</b>. Although, if you get an error during the process the other option is to manually install the module yourself;

Download the [pysqlcipher3 repository](https://github.com/rigglemania/pysqlcipher3/archive/refs/heads/master.zip) and extract it<br>
Open your terminal/command line and navigate to the folder you just extracted and type the following;

<b>Windows</b><br>
<code>python setup.py install</code>

<b>Linux/Mac OS</b><br>
<code>python3 setup.py install</code>

# Usage

The decryptor has been written into a class so you're able to call it at anytime. It requires 3 arguments which can be found below;

- key: The decryption key used to decrypt the database
- output: The path/name of what/where you want the decrypted database named/placed
- database: The current location of the encrypted database

A sample decryption call would look like the following<br>
<code>from client import decryption</code><br>
<code>decryption("9bf9c6ed9d53...", "global_database.db", "/database/database.db").decrypt_database()</code>
