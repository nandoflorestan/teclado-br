==========================================
Layouts de teclado brasileiro para Windows
==========================================

**Os drivers para Windows** têm seu código-fonte nos arquivos de
extensão ``.klc``.  Esse formato de arquivo é de um utilitário chamado
`Microsoft Keyboard Layout Creator <https://www.microsoft.com/en-us/download/details.aspx?id=22339>`_,
o programa que deve ser utilizado para editá-los.

Ao final do processo o programa gera instaladores .msi, os quais são incluídos
neste projeto num diretório chamado ``setup``, para conveniência dos usuários.


DICA VALIOSA para instalar o MSKLC
==================================

Se você pretende instalar o editor de teclados da Microsoft, linkado acima,
eis uma dica.

Escrevo em 2019 usando Windows 10.  O utilitário da Microsoft é antigo e nunca
foi atualizado.  O instalador pode não executar, dizendo necessitar do
*dotnet framework 2.0*, versão d'antanho que, baixada isoladamente e instalada,
não ajudou. Experimentei outras versões mais recentes do dotnet mas também não
possibilitaram a instalação do MSKLC.

Finalmente eis o procedimento que funcionou para mim: instalar o .NET
Framework 3.5 através do Painel de Controle.

Aperte a tecla Windows e digite "Windows Features" (ou provavelmente
"Recursos" se o teu Windows é em português) e pressione Enter.
Também dá para abrir o Painel de Controle e procurar ali.  Enfim,
o objetivo é abrir uma caixa de diálogo chamada "Turn Windows features
on or off" (ligar ou desligar recursos do Windows).

Ali há uma caixinha que diz ".NET Framework 3.5 (includes .NET 2.0 and 3.0)".
Habilite-a, aperte OK, espere a instalação e depois tente instalar o editor
de teclado.  Assim deverá funcionar.
