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

a) Aperte a tecla Windows junto com R.  Aparece uma caixa para digitar um comando.
b) Digite ``appwiz.cpl`` e aperte Enter. Abre-se a janela *Programs and features*.
c) Clique no link *Turn Windows features on or off* (ligar ou desligar recursos do Windows).
d) Dentre várias configurações, há uma que diz ".NET Framework 3.5 (includes
   .NET 2.0 and 3.0)".  Habilite-a, aperte OK e espere a instalação.
e) Tente instalar o editor de teclado.  Agora deverá funcionar.
