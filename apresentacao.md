# Roteiro da apresentação — 2 atos

> Use junto com `pitch.md` (o pitch cronometrado de 3–5 min e a divisão dos 3).
> Este arquivo é a **coreografia da demo** + **as respostas de defesa**.
> O tema do seminário é **Tailwind** (framework de CSS). React entra só pra
> mostrar componentização — não venda React como se fosse o tema.

---

## Os 2 atos (o que abrir, o que falar)

### Ato 1 — só Tailwind (o problema)
Abrir: `https://pedrom-dev-git.github.io/seminario-tailwind/aula-simples/`

Falar:
> "HTML puro + Tailwind, sem framework nenhum. Funciona e fica bonito.
> **Mas** olhem o código: o card está **copiado 3 vezes**, com a mesma lista de
> classes em cada um. Quero 30 produtos? 30 cópias. Quero mudar o estilo do card?
> Edito em 30 lugares. É a crítica clássica: *Tailwind polui o HTML*."

Mostrar o código lado a lado (3 `<div>` idênticos).

### Ato 2 — com framework (a solução)
Abrir: `https://pedrom-dev-git.github.io/seminario-tailwind/`

Falar + fazer ao vivo:
> "Mesmo visual. Mas agora o card foi escrito **uma vez** como componente.
> E — olhem — eu **adiciono um produto ao vivo** [digita, clica ＋] e a tela se
> atualiza sozinha. **Removo** [clica remover] e some. Não recarreguei a página."

Redimensionar a janela: grid vai de 1 → 2 → 3 colunas.
> "E nenhuma `@media` escrita à mão — é `grid-cols-1 sm:grid-cols-2
> md:grid-cols-3`. O `md:` vira media query sozinho."

Fechar:
> "O Tailwind é **idêntico** nos dois. O framework não mudou a aparência —
> ele tirou a repetição (componente) e deu vida à página (estado). A poluição
> ficou **encapsulada** dentro do componente, escrita uma vez."

---

## Perguntas que vão cair — e a resposta curta

**"Isso é JavaScript? Por que `type="text/babel"`?"**
> É **JSX**: JavaScript que deixa escrever HTML dentro. O navegador não entende
> JSX direto, então o **Babel** (um dos scripts CDN) traduz pra JS puro antes de
> rodar. `type="text/babel"` = "traduz isto primeiro". Em produção isso é feito
> no build (NPM/Vite); aqui via CDN pra não instalar nada.

**"Por que `class` num arquivo e `className` no outro?"**
> No HTML puro é `class`. No JSX é `className` porque JSX é JavaScript, e `class`
> já é palavra reservada em JS. Pra evitar a colisão, o React usa `className`.
> Mesma coisa, só o nome do atributo muda.

**"Pra que serve um framework?"**
> Pra não reconstruir a máquina básica toda vez: ele dá componentes reutilizáveis
> e faz a tela se atualizar sozinha quando os dados mudam. Tailwind é framework
> de **aparência** (CSS); React, de **estrutura** (UI). O seminário é sobre o
> primeiro.

**"O que o React faz especificamente?"**
> Mantém a tela sincronizada com os dados: você descreve a UI em componentes,
> muda o estado (`useState`/`setProdutos`), e ele recalcula e aplica **só a
> diferença** no HTML. Não cuida de estilo nem de backend — só dessa camada.

**"O HTML do Tailwind não fica poluído?"**
> Fica, se usado em HTML cru (Ato 1). Com framework (Ato 2) a sopa de classes
> vive **uma vez** dentro do componente e o resto fica limpo. Verbosidade vira
> preço fixo, não recorrente.

**"Por que Tailwind e não Bootstrap?"**
> Bootstrap entrega componentes prontos — rápido, mas todo site fica com "cara
> de Bootstrap". Tailwind dá as classes-tijolo: design próprio desde a 1ª linha.

**"Funciona sem instalar nada?"**
> Pra demo, sim — CDN (foi o que usamos). Pra produção, NPM/Vite gera só o CSS
> usado (bundle mínimo). Passo a passo dos dois no `COMO-RODAR.md`.

**"Tailwind 4 mudou da 3?"**
> Sim: motor novo em Rust (build mais rápido), config CSS-first
> (`@import "tailwindcss"`), container queries nativas. As classes no HTML
> continuam iguais.

---

## Analogia que cola (se a banca for técnica)

React = um **ALV pra tela inteira**: você não repinta célula por célula; mexe na
fonte de dados (internal table / `useState`) e o motor redesenha o que mudou.
`App()` ≈ a rotina que monta o grid; React a re-executa e aplica só o delta.

---

## Checklist do dia
- [ ] Internet testada na sala (CDN + Pages precisam de rede)
- [ ] Plano B offline aberto (zip local + gravação) caso a rede caia
- [ ] Cada um sabe responder QUALQUER pergunta acima (não só a "sua parte")
- [ ] As 2 URLs abertas em abas antes de começar
- [ ] Uso de IA citado conforme política da disciplina
- [ ] Confirmado com o Prof. se **trio** é aceito (enunciado diz "duplas")
