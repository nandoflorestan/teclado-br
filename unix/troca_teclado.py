#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''This program is public domain.'''

from __future__ import (absolute_import, division, print_function,
    unicode_literals)
import os
import sys
import shutil
import re

__author__    = "Nando Florestan"
__url__       = "http://nando.oui.com.br/"
__version__   = "0.05"
__date__ = "2012-04-09"


class Model:
    # === Configuration ===
    xorgFile  = "/etc/X11/xorg.conf"
    destFolders = ["/usr/share/X11/xkb/symbols",
                   "/usr/X11R6/lib/X11/xkb/symbols"]
    filesToCopy = ["brdk/brdk"]
    keyboards = [("abnt2", "br"  ,  ""          ),
                 ('abnt2', 'br'  ,  'dvorak'    ),
                 ("abnt2", "brdk",  ""          ),
                 ("abnt2", "brdk",  "shifted"   ),
                 ("abnt2", "br",    "nativo"    ),
                 ("abnt2", "br",    "nativo-epo"),
                 ("pc105", "br",    "nativo-us" ),
                 ("pc105", "us",    "intl"      ),
                 ("pc105", "us",    "dvorak"    ),
                 ("pt"   , "pt",    ""          ),
    ]
    # === end configuration ===

    @staticmethod
    def user_is_root():
        return os.geteuid() == 0

    @staticmethod
    def require_root():
        if not Model.user_is_root():
            raise RuntimeError(
                "Este programa requer privilegios de administrador.")

    def find_symbols_dir(self):
        for location in self.destFolders:
            if os.path.exists(location) and os.path.isdir(location):
                return location
        raise RuntimeError("Nao foi encontrado o diretorio symbols.")

    def assert_copied(self, file):
        # If the file already exists there, do nothing...
        fileName = os.path.basename(file)
        destination = os.path.join(self.destFolder, fileName)
        self.show("• Copiando o arquivo: " + fileName)
        #+ " para a pasta " + self.destFolder
        try:
            shutil.copy(file, self.destFolder)
        except:
            self.show("→ Não foi possível realizar a cópia. "
                "Verifique as permissões.")
            if os.path.exists(destination) and os.path.isfile(destination):
                self.show("  → Mas existe lá um arquivo com esse nome. "
                    "Continuando.")
            else:
                raise RunTimeError("Nao pude copiar: " + destination)

    def activate(self, keyb):
        command = "setxkbmap -model " + keyb[0] + " -layout " + keyb[1]
        if keyb[2] != "":
            command += " -variant " + keyb[2]
        exitCode = os.system(command)
        return exitCode

    def install(self, keyb):
        if not os.path.isfile(self.xorgFile):
            raise RuntimeError("Erro: Nao existe o arquivo a ser alterado: "
                               + self.xorgFile)
        backFile = self.xorgFile + ".TrocaTeclado"
        tempFile = self.xorgFile + ".temp"
        if os.path.isfile(backFile):
            self.show("Não será feito backup porque já existe: " + backFile)
        else:
            self.show("Criando backup: " + backFile)
            shutil.copy(self.xorgFile, backFile)

        inSection  = False
        inKeyboard = False
        changedModel   = False
        changedLayout  = False
        changedVariant = False
        regexKeyb1 = re.compile(r"identifier.+keyboard")
        regexKeyb2 = re.compile(r"driver.+kbd")
        input  = open(self.xorgFile, "r")
        output = open(tempFile, "w")
        try:
            for line in input:
                result = line
                lower = line.lower()
                trim = lower.strip()
                pos = -1
                if inSection and inKeyboard:
                    if trim.startswith("option"):
                        # If current line says the model, substitute it
                        pos = lower.find("\"xkbmodel\"")
                        if pos > -1:
                            output.write("#" + line)
                            changedModel = True
                            result = line[0:pos+10] + "\t" + quoted(keyb[0]) + "\n"
                        # If current line says the layout, substitute it
                        pos = lower.find("\"xkblayout\"")
                        if pos > -1:
                            result = line[0:pos+11] + "\t" + quoted(keyb[1]) + "\n"
                            output.write("#" + line)
                            changedLayout = True
                        # If current line says the variant, substitute it
                        pos = lower.find("\"" + "xkbvariant" + "\"")
                        if pos > -1:
                            result = line[0:pos+12] + "\t" + quoted(keyb[2]) + "\n"
                            output.write("#" + line)
                            changedVariant = True
                    if trim == "endsection":
                        if not changedModel:
                            output.write("\tOption\t\"XkbModel\"\t" + quoted(keyb[0]) + "\n")
                            changedModel = True
                        if not changedLayout:
                            output.write("\tOption\t\"XkbLayout\"\t" + quoted(keyb[1]) + "\n")
                            changedLayout = True
                        if not changedVariant:
                            output.write("\tOption\t\"XkbVariant\"\t" + quoted(keyb[2]) + "\n")
                            changedVariant = True
                elif trim == "endsection":
                    inSection  = False
                    inKeyboard = False
                elif trim == "section \"inputdevice\"":
                    inSection  = True
                elif regexKeyb1.match(trim) or regexKeyb2.match(trim):
                    inKeyboard = True
                output.write(result) # always write the line
        except:
            self.show("Erro ao modificar o arquivo " + tempFile)
            raise
        finally:
            input.close()
            output.close()
        # Tendo criado o arquivo temp, podemos apagar o atual e renomear o temp
        if changedModel and changedLayout and changedVariant:
            os.remove(self.xorgFile)
            shutil.copyfile(tempFile, self.xorgFile)
            self.show("Arquivo alterado com sucesso:           " + self.xorgFile)
            self.show("O leiaute escolhido tornou-se permanente.")
            return True
        else:
            self.show("Sinto muito. Não consegui compreender seu arquivo: " + \
              self.xorgFile)
            self.show("Não enxerguei as partes:")
            if not changedModel:
                self.show("model, ")
            if not changedLayout:
                self.show("layout, ")
            if not changedVariant:
                self.show("variant.")
            self.show("")
            self.show("Por favor explique o bug e envie para o autor "
                "o seu arquivo: ")
            self.show("  " + self.xorgFile)
            return False

    def __init__(self, printFunction):
        """Constructor of the Model class.
        It takes a "printFunction" parameter. This is a function from the user
        interface that shows messages to the user. This allows the Model class
        to display messages without caring whether the UI is graphical or a
        console.
        """
        self.show = printFunction
        self.require_root()
        self.destFolder = self.find_symbols_dir()
        self.show("Copiando para: " + self.destFolder)
        for file in self.filesToCopy:
            self.assert_copied(file)


# === Console user interface ===

greeting = """
troca_teclado versão %s (%s)
============= %s
Este programa permite TESTAR e INSTALAR alguns leiautes de teclado.
Esta versão instala só para o servidor X, e não para o console.
Portanto, deve ser executada no modo gráfico.
ATENÇÃO: Este programa só foi testado no Ubuntu Linux 8.04 Hardy Heron.
""" % (__version__, __date__, __url__)


def bool_input(prompt):
    opt = raw_input(prompt + "(Y/N) ")
    lopt = opt.lower()
    if lopt == "s" or lopt == "y": return True
    if lopt == "n": return False
    # Invalid answer, let's ask again
    return bool_input(prompt)


def menu():
    print("\n    MODEL  LAYOUT   VARIANT")
    for c, keyb in enumerate(m.keyboards):
        print(str(c + 1).rjust(2) + ". "         \
              + keyb[0].center(5) + '  ' \
              + keyb[1].center(6) + '  ' \
              + keyb[2].center(9))
    while True:  # Ask until we get a valid integer
        try:
            opt = int(raw_input("Numero do teclado desejado: ")) - 1
        except ValueError:
            continue
        else:
            if opt < 0 or opt > len(m.keyboards):
                continue
            break
    try:
        keyb = m.keyboards[opt]
    except:
        print("Opção inválida. Tchau.")
        sys.exit(4)
    activate(keyb)


def activate(keyb):
    print("\nAtivando o leiaute APENAS PARA ESTA SESSÃO...")
    exitCode = m.activate(keyb)
    if exitCode != 0:
        print("Erro: setxkbmap retornou {}".format(exitCode))
        sys.exit(5)
    print("OK, teclado ativado!")
    raw_input("Teste o leiaute digitando uma linha: ")
    if bool_input("Quer escolher outro leiaute? "):
        menu()
    else:
        install(keyb)


def quoted(s):
    return "\"" + s + "\""


def install(keyb):
    print('')
    if not bool_input("Quer instalar PERMANENTEMENTE o leiaute atual? "):
        print("Ao reiniciar o servidor X, "
            "seu antigo teclado voltará a vigorar.\n")
        sys.exit(0)
    try:
        if not m.install(keyb):
            sys.exit(2)
    except Exception as x:
        print(x)
    print


def show(msg):
    print(msg)


def main():
    print(greeting)

    global m
    try:
        m = Model(show)
    except RuntimeError as e:
        print(e)
        sys.exit(1)
    menu()


main()
