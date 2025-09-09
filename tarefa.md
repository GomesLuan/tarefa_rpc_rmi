# Descrição
-----------

Esta tarefa consiste na implementação de servidores RPC e RMI, para responder
às requisições realizadas por clientes que foram enviados juntos da atividade.

Para o desenvolvimento destas atividades, utilize uma máquina virtual
executando na AWS Academy. Os códigos solicitados deverão ser enviados na
Tarefa no SIGAA conforme data definida pelo professor.

As atividades são as seguintes:

# RPC
-----

1. Desenvolvimento de um servidor para um chat remoto com RPC.

O cliente já está disponível em 'chat/client.py'.

Este cliente recebe, em sua execução um 'nome' e uma 'mensagem' a ser enviada
para o servidor, através da função 'falar(nome, msg)'. As mensagens que já
estão no chat sao recebidas através da função 'mensagens()'.

As mensagens do chat são organizadas como uma tupla, da seguinte forma:

[
    (nome1: msg1),
    (nome2: msg2),
    ...
]

No servidor, é preciso implementar as funções e registrá-las no servidor. Pode
ver os slides da aula de RPC para ver os detalhes.


2. Desenvolvimento de um servidor RPC para controle de estoque distribuído.

Este servidor deve responder às requisições de um cliente, já disponibilizado
em 'estoque/client.py'.

As funções que o cliente requisita são:
- adicionar
- remover
- consultar
- estoque

Esta última retorna todo o estoque do servidor, que é implementado como um
discionário e tem o formato:

{
    produto1: qtd1,
    produto2: qtd2,
    ...
}

Assim como no caso do chat acima, o servidor precisa implementar as funções e registrá-las. Utilize os slides da aula de RPC para ver os detalhes.


# RMI
-----

3. Desenvolvimento de um servidor para o monitoramento de uma máquina remota via RMI

Esta tarefa consiste em utilizar a biblioteca Python
'psutil'(https://psutil.readthedocs.io/en/latest/) para fazer o monitoramento
de uma máquina remota via RMI.

O servidor, que está executando nesta máquina remota, atende às requisições do
cliente, que está disponível em 'monitoramento/client.py'. 

Para facilitar a implementação e o entendimento de como utilizar a biblioteca
'psutil', já está disponiblizada uma versão inicial do servidor em
'monitoramento/server.py'.

Nesta versão inicial, a classe Monitor já foi desenvolvida, atendendo aos
métodos 'CPU' e 'Memoria'. No entanto, é necessário que você desenvolva mais 2
opções de monitoramento, conforme sua escolha, sendo necessário adicionar no
servidor e alterar no cliente.

Além disso, para executar o serviço RMI, é preciso executar o pyro5-ns e
desenvolver as demais operações para registro do serviço oferecido pela classe
Monitor no servidor.

Verifique nos slides da aula de RMI sobre como realizar isto.

