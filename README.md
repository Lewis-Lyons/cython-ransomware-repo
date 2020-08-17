# Cython Ransomware

# !!!!Attention!!!!

This repo contains files which are potentially dangerous. Dowlnoad and/or run these files  at your own risk. Please ensure you do so in a secure environment.

# Project

This project is an investigation into the runtime and obfuscation improvements to be gained by augmenting Python based crypto ransomware with Cython.

As modern cyber threats evolve, we are seeing increased occurrences of crypto ransomware threats in the wild. At the same time, very high-level programming languages, such as Python, have seen drastically increased use within the last decade. Despite this popularity, these languages have not been viewed as attractive languages of choice for ransomware authors. This is illustrated by only a few instances yet appearing in the wild.  

In this research we investigated the Python language as a vector for ransomware development. More specifically we utilised a superset language known as Cython to attempt to mitigate some of Pythons classical failures in the domains of performance and data obfuscation. We conducted experiments to determine how ransomware runtime is distributed during executing and use these results to target specific key functions to attempt to improve runtimes. Further we proved Cythons’ capacity to translate code into the C language which can provide varying levels of obfuscation to Python ransomware.  

From our results we concluded that Cython has limited potential to increase runtime speeds of Python ransomware, assuming said ransomware is well designed. We found that pure Python already has access to features which make it well suited to ransomware development if they are understood. We also found that Cython could offer significant improvements over conventional methods of obscuring Python code.
