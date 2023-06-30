import subprocess
import os
from termcolor import colored






target = input("Passe o dominio: ")

def recon_subfinder(hosts):
    if isinstance(hosts, str):
        hosts = [hosts]

        for target in hosts:
            if target.startswith("http://"):
                target = target[7:]
            elif target.startswith("https://"):
                target = target[8:]
        print(colored("Coletando Sub-Dominios","yellow"))
        process = subprocess.run(["subfinder", "-d", target,"-silent"],  capture_output=True, text=True)
        with open("sub-finder-"+target+".txt", "a") as f:
            for line in process.stdout.split("\n"):
                f.write(line + "\n")
    

def enum_assetfinder(hosts):
    if isinstance(hosts, str):
        hosts = [hosts]

    for target in hosts:
        if target.startswith("http://"):
            target = target[7:]
        elif target.startswith("https://"):
            target = target[8:]
    print(colored("Coletando Sub-Dominios 2","green"))
    result = subprocess.run(["assetfinder", "--subs-only", target], capture_output=True, text=True)
    with open("assetfinder-"+target+".txt", "a") as f:
        for line in result.stdout.split("\n"):
            f.write(line + "\n")



def retirando_repetidos():
    print(colored("Retirando dados repetidos","blue"))
    with open("sub-finder-"+target+".txt", "r") as f1, open("assetfinder-"+target+".txt","r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        
    domains = set(lines1 + lines2)
    with open("unique_domains-"+target+".txt", "w") as f3:
        for domain in domains:
            f3.write(domain)
            

def extrai_para_permut():
    print(colored("Criando Lista para permutações","red"))
    with open("unique_domains-"+target+".txt", "r") as file:
        hostnames = [line.strip().split(".")[0] for line in file]
        with open("permut."+target+".txt", "w") as f:
            for hostname in hostnames:
                f.write(hostname + "\n")



def Brute_permution():
    print(colored("Criando Sub-dominios apartir de permutações", "green"))

    result = subprocess.run(["dmut", "-u", target, "-d", "permut."+target+".txt", "-w", "100", "--dns-timeout", "300","--dns-retries", "5", "--dns-errorLimit", "25"], capture_output=True, text=True)
    with open("dns-permutados-"+target+".txt", "w") as f:
        for line in result.stdout.split("\n"):
            f.write(line + "\n")



def retirando_repetidos_2():
    print(colored("Retirando dados repetidos e colocando os dns-permutados","blue"))
    with open("unique_domains-"+target+".txt", "r") as f1, open("dns-permutados-"+target+".txt","r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        
    domains = set(lines1 + lines2)
    with open("Todos-dominios-"+target+".txt", "w") as f3:
        for domain in domains:
            f3.write(domain)


#removendo linhas 
def remove_lines():
    with open("Todos-dominios-"+target+".txt", "r") as file:
        lines = file.readlines()
    with open("Todos-dominios-completos-"+target+".txt", "w") as new_file:
        for line in lines:
            if "|" not in line:
                new_file.write(line)
            
                



def excluindo_lista_n_usadas():
    os.remove("sub-finder-"+target+".txt")
    os.remove("assetfinder-"+target+".txt")
    os.remove("unique_domains-"+target+".txt")
    os.remove("permut."+target+".txt")
    os.remove("dns-permutados-"+target+".txt")
    os.remove("Todos-dominios-"+target+".txt")










recon_subfinder(target)
enum_assetfinder(target)
retirando_repetidos()
extrai_para_permut()
Brute_permution()
retirando_repetidos_2()
remove_lines()
excluindo_lista_n_usadas()
print(colored(f"Checando os Dominios encontrados do {target}","green"))
print(colored(f"Resolvendo os ip de cada dns do {target}","red"))
