# Post-Mortem — Missão de Release

## Time
- Tech Lead: Luiz Miguel Freitas Marques
- Dev A: Paulo Junior
- Dev B: Pedro Victor
- QA/Release: Miguel Marques, Paulo Junior, Pedro Victor

---

## O que funcionou bem
Depois do entendendimento do fluxo (branches, pull requests), a criação das branches e pull requests, e do fluxo de trabalho em geral, ficou facil de compreender. Com isso, 
O trabalho com branches separadas funcionou bem, pois cada integrante conseguiu desenvolver sua parte sem atrapalhar os demais, alem disso, a review e o merge de pull requests funcionou bem e sem problemas.

## O que deu errado ou foi difícil
No inicio, foi complicado conseguir entender o fluxo que deveria ser feito e a criação de branches e PRs era bastante abstrato. A parte de aceitar e criar os pulls requests era 
em parte dificil, pois ficava em lugares "escondidos" e nao sabiamos como fazer eles. Mas a pior parte em si mais dificil, foi a manipulação de branches, e funcionalidades como o rebase e o pull para manter elas atualizadas e evitar conflitos, dentre outras dificuldades.

## Onde usamos rebase (e por quê)
Usamos o rebase para atualizar cada branch com as alterações que foram realizadas por cada dev, permitindo a resolução antecipada dos conflitos.

## Onde usamos merge (e por quê)
Usamos o merge para conseguir juntar as branches criadas por cada dev, atualizando, por exemplo a develop com as alterações do dev-a, e posteriormente atualizando a main com as alterações feitas na develop. Ele é necessario para que possa mesclar as branches.

## O que faríamos diferente
Foram criadas branches e realizados commits desnecessários devido à falta de experiência com Git, o que resultou em um histórico de commits mais poluído do que o planejado.
Para evitar esse problema em projetos futuros, realizaríamos um planejamento prévio das alterações, da estratégia de branches e da organização dos commits antes do início do desenvolvimento. Isso contribuiria para um fluxo de trabalho mais organizado e um histórico mais limpo e fácil de revisar.
