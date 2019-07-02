BRDK - drivers inovadores para teclado brasileiro
=================================================

Este pacote contém os seguintes drivers:

- Teclado Dvorak brasileiro, para Unix, Mac e Windows (XP, Vista, 7, 10 etc.)
- Teclado brasileiro nativo, para Unix e Mac

Por que usar um teclado Dvorak?
-------------------------------

Vide http://dev.nando.audio/pages/teclado.html

Status do projeto
-----------------

**Os drivers para Windows** têm seu código-fonte nos arquivos de
extensão .klc.  Esse formato de arquivo é de um utilitário chamado
Microsoft Keyboard Layout Creator, o programa que deve ser utilizado para
editá-los.  Ao final do processo o programa gera instaladores .msi.

**Os drivers para Unix** que temos aqui funcionam bem mas são ligeiramente
obsoletos, pois Ari Caldeira os melhorou um pouco e conseguiu incluí-los no
código-fonte do `x.org`_. Ou seja, hoje em dia todas as distribuições do
Linux já vêm com uma versão melhorada desses drivers de teclado.
A versão que está neste pacote é a original, elaborada principalmente por
Nando Florestan, Heitor Moraes e Luiz Portella em 2005 e 2006.

**Os drivers para Mac** foram criados com o utilitário open source `Ukelele <https://scripts.sil.org/ukelele>`_ em 2019 por Victor Fonseca (Dvorak BR) e 2014 por amagnoni (brasileiro nativo). Para instalar, basta copiar os arquivos .bundle para “/Library/Keyboard Layouts/”, fazer logout (ou reiniciar a máquina) e depois ir em “System Preferences –> Keyboard –> Input Sources” e habilitar os leiautes de teclado. Os teclados de Mac seguem o padrão americano e, portanto, tem 2 teclas a menos do que os teclados ABNT. Por essa razão, esses leiautes não possuem as teclas "ç" e "\\". O leiaute da tecla "option" foi mantido como no original (Dvorak americano).

Mas e os **outros sistemas operacionais**?

Colaboração open source é bem-vinda e por isso é que os fontes estão no
`github <https://github.com/victor-fonseca/teclado-br>`_.
Para quaisquer outras ideias, pode
`criar um ticket <https://github.com/victor-fonseca/teclado-br/issues>`_.

troca_teclado
-------------

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

Créditos
--------

Os arquivos deste projeto são resultado do trabalho de:

- Ari Caldeira (criador do Brasileiro Nativo; novo brdk p/ Unix)
- `Gabriel Marquez <https://github.com/gblmarquez>`_
  (novos drivers brdk p/ Windows)
- Heitor Moraes (brdk e documentação)
- Luiz Portella (brdk p/ Unix)
- `Nando Florestan <https://github.com/nandoflorestan>`_
  (brdk p/ Unix e Windows e documentação)
- `Victor Fonseca <https://github.com/victor-fonseca>`_
  (brdk p/ Mac e documentação)
- `amagnoni <https://github.com/amagnoni>`_
  (br nativo p/ Mac)

Contribua
---------

Ao fazer um pull request neste projeto, você concorda em
doar o seu trabalho para o domínio público.
