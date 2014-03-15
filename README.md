telemob
=======

Telemob: ferramenta para ajudar a sociedade civil a pressionar seus deputados e senadores no Congresso Nacional

Sua motivação inicial é facilitar a pressão popular pela aprovação do Marco Civil da Internet, otimizando e distribuindo a pressão entre todos os congressistas.

Idéia: https://garoa.net.br/wiki/Telemob

Grupo de discussão para desenvolvedores: https://groups.google.com/forum/#!forum/telemob



Exemplo de uso: campanha pela aprovação do Marco Civil da Internet
==================================================================

Não adianta todo mundo ligar só para os líderes, ou para os deputados mais famosos ou para o Eduardo Cunha (PMDB-RJ) -- que é totalmente contra o Marco Civil.

É preciso ligar para todos os congressistas, de todos os partidos e estados. Se cada congressista receber muitas ligações, a chance de votarem direito aumenta muito.

O '''Telemob''' direciona as pessoas para ligarem para os congressistas de seus estados, e ligarem primeiro para aqueles que ainda receberam menos ligações.


Descrição
===========

Tela 1: Entrada
-----------------

Exibe:

* '''título''' e '''resumo''' da campanha atual (futuramente poderá haver mais de uma campanha)

* Instrução: "Escolha o estado onde você vota (seu domicílio eleitoral)"

* Lista clicável de unidades da federação

Ação:

* O usuário clica em uma unidade da federação e vai para a lista de deputados (futuramente poderá ser a lista de senadores, conforme configurado na campanha ativa)

Tela 2: Lista de Congressistas
-------------------------------

Exibe:

* Lista de congressistas da UF selecionada, ordenada por prioridade de chamada. A prioridade é definida pelo inverso do número de cliques que o deputado já recebeu. Assim no topo da lista aparecem aqueles que sofreram menos pressão até o momento.

* Instrução: "Escolha o deputado para você ligar. Dê preferência ao primeiro da lista."

Ação:

* O usuário clica em um deputado e vai para a Tela de Ligação

Tela 3: Apoio à Ligação
-------------------------------

Exibe:

* Nome, partido, telefones e e-mail do congressista.

* Textos preparados para ajudar a pessoa a comunicar os pontos principais da campanha.

Ação:

* Usuário aciona caixas de verificação (checkboxes) e botões de rádio (radio buttons) para indicar qual ou quais contatos ele fez ou tentou fazer.

```
 [ ] Telefonei
     ...e o resultado foi:
     (x) Falei com a/o Deputada/o em pessoa  | 13 pontos
     ( ) Falei outra pessoa                  |  5 pontos
     ( ) Deixei recado em uma máquina        |  3 pontos
     ( ) Número ocupado                      |  1 ponto
     ( ) Ninguém atendeu                     |  1 ponto
     ( ) Número inexistente ou outra falha   |  1 ponto
 [ ] Mandei telegrama                        |  8 pontos
 [ ] Enviei fax
     ...e o resultado foi:
     (x) Transmissão bem sucedida            |  5 pontos
     ( ) Número ocupado                      |  1 ponto
     ( ) Ninguém atendeu                     |  1 ponto
     ( ) Número inexistente ou outra falha   |  1 ponto
 [ ] Enviei e-mail                           |  2 pontos
```


Tela 4: Apoio à Ligação
-------------------------------

Sumário dos contatos feitos e links para o usuário contar nas redes sociais que colaborou com a campanha X no Telemob, marcando X "pontos de pressão".



Como funciona a pontuação
==========================

A pontuação serve para indicar ao usuário a forma mais eficaz de contato, e também para reordenar os deputados conforme a quantidade e qualidade dos contatos recebidos, colocando os que foram menos contatados no topo da lista da tela 3.

Obs: O telegrama é altamente eficaz: não tem linha ocupada e com certeza algum assessor vai ler. E-mail é fácil de ignorar.

Telegramas podem ser enviados via Internet. Custa a partir de R$ 4.98 http://shopping.correios.com.br/wbm/store/script/wbm2400901p01.aspx?cd_company=ErZW8Dm9i54=&cd_product=IFYzQdTZeXo=

