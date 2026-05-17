# Onde entra o framework (React/Astro) — e por que fica melhor

## O problema do `aula-simples/index.html`

Lá, o card aparece **3 vezes copiado**:

```html
<div class="bg-white p-5 rounded-xl shadow flex flex-col gap-2"> … Fone … </div>
<div class="bg-white p-5 rounded-xl shadow flex flex-col gap-2"> … Teclado … </div>
<div class="bg-white p-5 rounded-xl shadow flex flex-col gap-2"> … Webcam … </div>
```

A "sopa de classes" Tailwind está **duplicada em cada card**. 3 produtos → 3 cópias.
30 produtos → 30 cópias. Quer trocar `rounded-xl` por `rounded-2xl`? Edita nos 30 lugares.
**É essa duplicação que você sentiu como "poluído".**

## O que o framework faz

React/Astro/Vue/Svelte introduzem **componente**: um pedaço de UI nomeado e reutilizável.

```jsx
function Card({ nome, desc }) {
  return <div className="bg-white p-5 rounded-xl shadow flex flex-col gap-2"> … </div>;
}
```

A sopa de classes aparece **uma única vez** — dentro do `Card`. O uso fica limpo:

```jsx
<div className="grid grid-cols-1 md:grid-cols-3 gap-4">
  {produtos.map(p => <Card nome={p.nome} desc={p.desc} />)}
</div>
```

Trocar `rounded-xl` → edita **1 lugar**. Adicionar 27 produtos → muda só o array de dados,
o markup não cresce.

## Antes × depois

| | `aula-simples/` (HTML puro) | `com-framework/` (React) |
|---|---|---|
| Onde mora a classe Tailwind | repetida em todo card | 1 vez, no componente `Card` |
| Adicionar produto | copia/cola o bloco inteiro | +1 linha no array de dados |
| Mudar o estilo do card | edita N lugares | edita 1 lugar |
| HTML que você lê no dia a dia | sopa de classes | `<Card />` limpo |

> A poluição não some — ela fica **encapsulada**. Você paga a verbosidade uma vez,
> dentro do componente, e nunca mais olha pra ela.

## Por que isso responde "Tailwind é poluído?"

A crítica "Tailwind polui o HTML" só vale **sem componente**. Com framework, o
utility-first vira vantagem: o estilo está colado ao componente (fácil deletar,
zero CSS órfão) **e** o HTML de uso fica limpo. É por isso que Tailwind quase nunca
é usado em `.html` cru — anda **sempre junto** de React/Astro/Vue. Os seus projetos
`turismo` e `pedrom-site` fazem exatamente isso: Tailwind dentro de componentes
`.astro`, por isso o HTML deles não parece poluído.

## Sobre esta demo

`index.html` roda React **via CDN, sem build** (igual ao Tailwind CDN) — dá pra abrir
com 2 cliques e mostrar em aula. Resultado visual é **idêntico** ao `aula-simples/`;
o que mudou é a organização do código, não a tela.

> Em projeto real (não demo) usa-se build — `npm create astro` / `npm create vite` —
> que ainda gera CSS/JS mínimo. O CDN aqui é só pra provar o conceito sem instalar nada.

## No pitch

Frase de efeito pra fechar a parte de "desvantagens":

> "Dizem que Tailwind polui o HTML. Poluiria — se você usasse em HTML cru. Mas
> Tailwind anda com React/Astro: a classe vive **uma vez** dentro do componente,
> e o resto do código fica limpo. A verbosidade vira preço fixo, não recorrente."
