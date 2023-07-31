# Layouts de teclado para o X (Linux etc.)

Os drivers que atualmente temos neste diretório são obsoletos porque usam
```keymap```.  Todas as distribuições do Linux já vêm com drivers melhores.

Foi Ari Caldeira quem escreveu as novas versões e conseguiu incluí-las no
código-fonte do `x.org`. Ou seja, hoje em dia todas as distribuições do
Linux já vêm com uma versão melhorada destes drivers de teclado.
A versão que está neste pacote é a original, elaborada principalmente por
Nando Florestan, Heitor Moraes e Luiz Portella em 2005 e 2006.

**Para criar layouts novos consulte:**

- [http://www.xfree86.org/current/XKB-Enhancing.html](http://www.xfree86.org/current/XKB-Enhancing.html)
- [https://wiki.archlinux.org/index.php/X_keyboard_extension](https://wiki.archlinux.org/index.php/X_keyboard_extension)

## Layout Atualizado com Movimentação

O código-fonte em `x.org`_ foi reescrito adicionando em [[2023-07-31]] 
o uso das teclas `C, H, T, N`_ em conjunto com o modificador `ALT-R/ALTGR`_ 
funcionarem como as setas do teclado, facilitando a permanência das mãos
na Home Row. 

Embora fosse melhor ter o uso das setas na mão esquerda - considerando a 
posição do modificador, os signos que estavam setados para aparecer quando
acionada a tecla com o modificador eram pouco usados comparados ao seguinte
esquema:

| Tecla | Tecla + ALTGR | Tecla Comparada | Tecla Comp + ALTGR |
| ---------: | :----------------------- | -------------: | :-------------- |
| C | ç | . | • |
| H | ħ | o | œ | 
| T | ŧ | e | € |
| N |   | u | ← |

Assim, levando em consideração que já existe uma tecla dedicada para o `Ç`, 
e também que as grafias `ħ, Ħ, ŧ e Ŧ` são pouco utilizadas em comparação com 
`œ, Œ, €`, e que, por vezes as pessoas podem trabalhar com sistema monetário
para a utilização do símbolo do Euro, ou com termos em Latim, para utilizar
as elisões com `o` e `e`, foi preferível utilizar as teclas acima mencionadas,
ainda que o polegar cause um pouco de tensão ao precionar o modificador.

Além disso, decidi manter o padrão adquirido do antigo `LK201`, que primeiro 
dispôs das teclas de movimento do cursor no conhecido *Inverted-T* layout,
facilitando o uso. 

# troca_teclado (obsoleto)

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
