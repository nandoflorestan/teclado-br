========================================
Layouts de teclado para o X (Linux etc.)
========================================

Os drivers que atualmente temos neste diretório são obsoletos porque usam
``keymap``.  Todas as distribuições do Linux já vêm com drivers melhores.

Foi Ari Caldeira quem escreveu as novas versões e conseguiu incluí-las no
código-fonte do `x.org`_. Ou seja, hoje em dia todas as distribuições do
Linux já vêm com uma versão melhorada destes drivers de teclado.
A versão que está neste pacote é a original, elaborada principalmente por
Nando Florestan, Heitor Moraes e Luiz Portella em 2005 e 2006.

**Para criar layouts novos consulte:**

- http://www.xfree86.org/current/XKB-Enhancing.html
- https://wiki.archlinux.org/index.php/X_keyboard_extension


troca_teclado (obsoleto)
========================

É um utilitário para Unix, escrito por Nando Florestan na linguagem Python 2.x.
Serve para facilmente testar e instalar os leiautes de teclado.
Funcionava bem na época do Ubuntu Linux 8.04 "Hardy Heron".
Continua funcionando nas mais novas versões do Linux para testar os leiautes,
mas não para instalá-los permanentemente. Não há nenhum perigo em executar
o troca_teclado.

Para executá-lo, abra um console e, no diretório "unix", digite::

  sudo ./troca_teclado.py

Será pedida a senha do administrador do sistema.
Daí basta seguir as instruções na tela.

Nos bastidores, este programa executa o utilitário *setxkbmap*.

O código-fonte é de domínio público.

.. _x.org: http://www.x.org/
