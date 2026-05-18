# Pitch — Tailwind CSS (3 a 5 min)

> **Objetivo:** convencer a "equipe de desenvolvimento" a adotar Tailwind.
> **Formato:** 3 pessoas. Divisão: **João C.** abre (gancho + proposta) ·
> **Carlos** faz a demo ao vivo · **Pedro Mendonça** fecha (vantagens + prova).
> Perguntas no fim são de todos. Ensaiar com cronômetro.

---

## Roteiro cronometrado

### [0:00–0:30] Gancho — o problema (João C.)
> "Quanto do CSS do último projeto de vocês ainda está sendo usado? Ninguém sabe.
> Todo projeto CSS puro vira o mesmo filme: nomes de classe inventados
> (`.card-inner-wrapper-2`), media queries espalhadas, e um arquivo de estilo que
> só cresce e ninguém tem coragem de apagar nada."

### [0:30–1:30] A proposta — utility-first (João C.)
> "Tailwind inverte isso. Em vez de escrever CSS, você **compõe classes utilitárias
> direto no HTML**: `flex`, `p-4`, `text-center`. Você nunca sai do HTML, nunca
> inventa nome de classe, e — o ponto que importa — o CSS final tem **só o que
> você usou**. O motor JIT varre o projeto e gera o mínimo. Bundle de poucos KB,
> independente do tamanho do projeto."

### [1:30–3:00] Demonstração ao vivo (Carlos — abre a URL / `index.html`)
Mostrar na tela, narrando (corresponde ao app real `index.html`):
1. **Box model** — apontar um card: `class="bg-white p-5 rounded-xl shadow"` →
   "padding, cantos e sombra numa escala pronta. Acabou o '13px aleatório'."
2. **Interatividade (React + estado)** — digitar um nome, clicar **"＋ Adicionar"**:
   um card novo aparece. Clicar **"remover"**: some.
   > "Não recarreguei a página nem editei o HTML. Mudou o **estado** (`useState`),
   > o React redesenhou só o que mudou. Isso é componente + estado."
3. **Responsividade — o golpe:** redimensionar a janela; o grid vai de
   **1 → 3 colunas**.
   > "Reparem: **nenhuma `@media` escrita à mão**. É `grid-cols-1 md:grid-cols-3`.
   > O `md:` compila pra media query sozinho — responsividade declarativa, no HTML."

### [3:00–4:00] Vantagens × custo honesto (Pedro Mendonça)
- ✅ CSS mínimo · zero CSS morto · responsividade declarativa · design próprio.
- ⚠️ "O custo existe e a gente não esconde: o HTML fica verboso e tem uma curva
  pra decorar as utilities. **Mas** isso resolve com componentização — e o ganho
  de manutenção paga em poucas semanas."

### [4:00–4:45] Prova de produção + fechamento (Pedro Mendonça)
> "Isso não é teoria de tutorial: dois sites em produção nossos rodam **Tailwind 4
> em Astro** hoje. Instalação real é literalmente `npm install tailwindcss
> @tailwindcss/vite` e **uma linha** de CSS: `@import "tailwindcss"`.
> Para o que a gente faz — produtos e landing pages com identidade visual própria —
> Tailwind é a escolha que mais paga o investimento. **Recomendamos adotar.**"

### [4:45–5:00] Perguntas
Reservar para dúvidas técnicas (vale 20% — "capacidade de resposta").

---

## Munição para perguntas difíceis (decorar)

**"O HTML não fica poluído / ilegível?"**
> Fica mais longo, sim. Mas o estilo passa a viver junto do elemento — você lê o
> componente e sabe a aparência sem caçar num `.css`. Em projeto real, componentização
> (Astro/React) encapsula isso. É troca consciente: verbosidade local por zero CSS global órfão.

**"E performance?"**
> Melhora. O JIT gera só as classes usadas — bundle de poucos KB gzip que **não cresce**
> com o projeto, cresce com a variedade de estilos. CSS puro tende a acumular regra morta.

**"Por que não Bootstrap?"**
> Bootstrap é component-based: entrega `.btn`, `.card` prontos — rápido, mas todo site
> fica com "cara de Bootstrap" e customizar é brigar com o framework. Tailwind dá os
> tijolos, não a casa pronta: design próprio desde a primeira linha.

**"Funciona sem build?"**
> Pra protótipo/demo, sim — CDN `@tailwindcss/browser@4` (foi o que usamos aqui).
> Pra produção, não: o build local gera CSS muito menor. É a única exigência real.

**"Como customizo cores/espaçamentos da marca?"**
> Na v4, via `@theme` no próprio CSS — sem `tailwind.config.js` no caso comum.
> Define o token uma vez, usa como utility no projeto todo.

**"Tailwind 4 mudou muito da 3?"**
> Sim: motor novo em Rust (Oxide, build muito mais rápido), config CSS-first
> (`@import "tailwindcss"` substitui o `@tailwind base/components/utilities`),
> container queries nativas. A sintaxe das utilities no HTML continua igual.

---

## Checklist de ensaio
- [ ] Cronometrar — alvo 4:30, teto 5:00
- [ ] Testar o `index.html` no navegador ANTES (CDN exige internet na sala)
- [ ] Plano B: salvar um print/gravação do grid responsivo caso a internet caia
- [ ] Cada um sabe responder QUALQUER pergunta da munição (não só "a sua parte")
- [ ] Citar uso de IA conforme política da disciplina
