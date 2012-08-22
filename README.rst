BRDK - drivers inovadores para teclado brasileiro
=================================================

Este pacote contém os seguintes drivers:

- Teclado Dvorak brasileiro, para Unix e Windows (XP, Vista, 7 etc.)
- Teclado brasileiro nativo, para Unix. Autor: Ari Caldeira

Por que usar um teclado Dvorak?
-------------------------------

Vide http://nando.oui.com.br/pages/teclado.html

Status do projeto
-----------------

**Os drivers para Unix** que temos aqui funcionam bem mas são ligeiramente
obsoletos, pois Ari Caldeira os melhorou um pouco e conseguiu incluí-los no
código-fonte do `x.org`_. Ou seja, hoje em dia todas as distribuições do
Linux já vêm com uma versão melhorada desses drivers de teclado.
A versão que está neste pacote é a original, elaborada principalmente por
Nando Florestan, Heitor Moraes e Luiz Portella em 2005 e 2006.

Mas e os **outros sistemas operacionais**?

Seria bom se alguém criasse uma versão do teclado para **Macintosh**.
Colaboração open source é bem-vinda e por isso é que os fontes estão no
`github <https://github.com/nandoflorestan/teclado-br>`_.
Para quaisquer outras ideias, pode
`criar um ticket <https://github.com/nandoflorestan/teclado-br/issues>`_.

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

Contribua
---------

Ao fazer um pull request neste projeto, você concorda em
doar o seu trabalho para o domínio público.
