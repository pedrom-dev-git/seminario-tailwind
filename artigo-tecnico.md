# Tailwind CSS — Mini Artigo Técnico

> **Disciplina:** Desenvolvimento Web · **Prof.:** Iuri Santos · Unilasalle 2026/1
> **Framework:** Tailwind CSS (utility-first) · **Versão de referência:** 4.2.x
> **Dupla:** _[preencher nomes]_

---

## 1. Introdução — histórico e filosofia

Tailwind CSS é um framework **utility-first**: em vez de entregar componentes prontos
(um `.btn`, um `.card`), ele entrega centenas de **classes atômicas de uma única
responsabilidade** — `p-4` (padding), `flex`, `text-center`, `rounded-lg` — que você
**compõe diretamente no HTML** para construir qualquer design.

**Linha do tempo:**

| Ano | Marco |
|-----|-------|
| 2017 | Adam Wathan lança a v0.1, cunhando o termo *utility-first* |
| 2019 | v1.0 — adoção em massa |
| 2020–2021 | v2.0 e v3.0 — motor **JIT** (Just-In-Time): só gera o CSS das classes realmente usadas |
| 2025 | **v4.0** — novo motor **Oxide** (escrito em Rust, build ~5–10× mais rápido), configuração **CSS-first** (`@import "tailwindcss"` + `@theme`), *container queries* nativas, detecção automática de conteúdo — dispensa o `tailwind.config.js` no caso comum |

### Utility-first vs. Component-based

| | **Component-based** (Bootstrap, Bulma) | **Utility-first** (Tailwind) |
|---|---|---|
| Unidade | Componente pronto (`.card`, `.navbar`) | Classe atômica (`.p-4`, `.flex`) |
| Customização | Sobrescrever CSS / variáveis Sass | Recompor classes; sem fugir do framework |
| "Cara" do site | Tende ao visual padrão do framework | Design 100% próprio desde o início |
| Curva inicial | Baixa (cola o componente) | Média (decorar o vocabulário de classes) |

A filosofia central: **você nunca sai do HTML para estilizar**, e o CSS final contém
**apenas** o que foi usado — não o framework inteiro.

---

## 2. Como o Tailwind manipula Box Model, Flexbox e Responsividade

> *(Núcleo do critério "Domínio Técnico" — 40% da nota.)*

### Box Model
Cada propriedade do box model vira uma escala consistente (`0, 1, 2, 4, 8…` → `0.25rem` cada passo):

```html
<div class="m-4 p-6 border-2 border-gray-300 box-border w-64 h-40">
  <!-- margin:1rem · padding:1.5rem · border:2px · box-sizing:border-box -->
</div>
```

`m-` margin · `p-` padding · `border-` borda · `w-`/`h-` dimensão ·
`box-border`/`box-content` controla o `box-sizing`. Direcionais: `pt-` (top),
`px-` (eixo X), `mb-` (bottom), etc.

### Flexbox
```html
<nav class="flex items-center justify-between gap-4">
  <!-- display:flex · align-items:center · justify-content:space-between · gap:1rem -->
</nav>
```
`flex` · `flex-col` (direção) · `items-*` (align-items) · `justify-*`
(justify-content) · `gap-*` · `flex-1`/`grow`/`shrink`.

### Responsividade — *mobile-first* por prefixo de breakpoint
Sem escrever uma única `@media` à mão. As classes valem do breakpoint **para cima**:

```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <!-- 1 coluna no mobile · 2 a partir de 768px · 3 a partir de 1024px -->
</div>
```

| Prefixo | Largura mínima |
|---------|----------------|
| `sm:` | 640px |
| `md:` | 768px |
| `lg:` | 1024px |
| `xl:` | 1280px |
| `2xl:` | 1536px |

Internamente o prefixo `md:grid-cols-2` **compila para uma `@media (min-width:768px)`** —
o framework escreve a media query por você. A v4 ainda traz **container queries**
(`@container` / `@md:`) para responsividade relativa ao componente, não à viewport.

---

## 3. Vantagens e Desvantagens (vs. CSS3 puro)

### Vantagens
- **CSS final mínimo:** o motor JIT gera só as classes usadas. O bundle não cresce com o projeto — cresce com a *variedade* de estilos. Em produção fica tipicamente na casa de poucos KB gzip.
- **Zero troca de contexto:** estiliza no HTML; não pula entre `.html` e `.css` nem inventa nomes de classe (`.card-wrapper-inner-2`).
- **Design system embutido:** a escala de espaçamento, cores e tipografia já é consistente — difícil produzir o "espaçamento de 13px aleatório".
- **Responsividade declarativa:** `md:`, `lg:` em vez de gerenciar blocos de `@media` espalhados.
- **Manutenção local:** apagar o HTML do componente apaga junto todo o estilo dele — não sobra CSS órfão.

### Desvantagens
- **HTML verboso:** `class="flex items-center justify-between gap-4 px-6 py-3 …"` — longas listas de classe. Mitiga-se com componentização (Astro/React) ou `@apply`.
- **Curva de vocabulário:** é preciso decorar/consultar o nome das utilities no início.
- **Precisa de build no uso sério:** o JIT roda em build (Vite/PostCSS). O CDN existe, mas não é recomendado para produção.
- **Revisão de diff:** mudança de layout aparece como diff de HTML, não de CSS — incomoda quem espera o estilo separado.

### Comparativo direto

| Aspecto | CSS3 puro | Tailwind |
|---------|-----------|----------|
| Nomear classes | Manual (e propenso a inconsistência) | Não nomeia — usa utilities |
| Media queries | Escritas e mantidas à mão | `md:`/`lg:` geram automático |
| Tamanho final | Cresce e acumula CSS morto | Só o que é usado (JIT/purge) |
| Consistência visual | Depende de disciplina | Escala imposta pelo design system |
| Setup | Zero | Build (ou CDN para protótipo) |

---

## 4. Casos de uso

**Recomendado quando:**
- Design **próprio/único** (landing pages, produtos, sites de marca) — é o forte do utility-first.
- Times que querem **consistência sem CSS architecture pesada** (BEM, ITCSS).
- Stack com build moderno (Vite, Next, Astro) e componentização.
- Prototipagem rápida com fidelidade visual alta.

**Pensar duas vezes quando:**
- Página estática trivial, uma só, sem build → CSS puro pode ser mais simples.
- Time que precisa de **componentes prontos imediatos** sem querer desenhar nada → Bootstrap/Bulma entregam mais rápido.
- Restrição forte de não poder ter etapa de build.

**Exemplo de produção (referência da própria dupla):** os projetos `turismo` e
`pedrom-site` rodam **Tailwind 4.2** em produção (Astro + plugin `@tailwindcss/vite`).
Classes reais extraídas desses projetos:

```html
<section class="max-w-5xl mx-auto px-4 sm:px-6 py-12 md:py-16">
  <h2 class="text-4xl md:text-5xl font-bold text-dark-gray mb-4">…</h2>
  <img class="w-full h-64 md:h-80 object-cover" …>
</section>
```

---

## 5. Instalação

### Opção A — CDN (zero build, ideal para a apresentação/live coding)

Tailwind v4 publica um build *browser* standalone. Basta uma tag `<script>`:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body>
  <h1 class="text-3xl font-bold text-blue-600">Funciona na hora</h1>
</body>
</html>
```

> Ótimo para demo/protótipo. **Não use em produção** — o build local gera CSS muito menor e mais rápido.

### Opção B — NPM + Vite (produção, como nos projetos reais da dupla)

```bash
npm install tailwindcss @tailwindcss/vite
```

`vite.config.ts` (ou `astro.config.mjs`):

```js
import tailwindcss from '@tailwindcss/vite';

export default {
  vite: { plugins: [tailwindcss()] }
}
```

CSS de entrada (`src/styles/global.css`) — **uma linha** na v4:

```css
@import "tailwindcss";
```

Pronto. O motor detecta as classes usadas no projeto automaticamente e gera só o CSS
necessário. Sem `tailwind.config.js` no caso comum — customização via `@theme` no
próprio CSS.

---

## 6. Conclusão (gancho do pitch)

Tailwind troca "escrever CSS" por "compor um vocabulário consistente direto no HTML".
O custo é um HTML mais verboso e decorar utilities; o retorno é **CSS final mínimo,
zero CSS morto, responsividade declarativa e design próprio sem brigar com o
framework**. Para o cenário deste seminário — produto/landing com identidade visual —
é a escolha que mais paga o investimento.

---

## Referências

1. Tailwind CSS — Documentação oficial. <https://tailwindcss.com/docs>
2. Tailwind CSS v4.0 — Anúncio oficial do release. <https://tailwindcss.com/blog/tailwindcss-v4>
3. WATHAN, Adam. *CSS Utility Classes and "Separation of Concerns"*. adamwathan.me, 2017.
4. MDN Web Docs — Box Model / Flexbox / Media Queries. <https://developer.mozilla.org/>
5. Código de produção próprio: projetos `turismo` e `pedrom-site` (Tailwind 4.2, Astro).

---

> **Nota de integridade acadêmica:** este documento foi produzido com assistência de IA
> como base de pesquisa e estruturação. A dupla deve ler, entender, validar tecnicamente
> e **citar o uso de IA** conforme a política da disciplina antes de submeter. O domínio
> técnico cobrado no pitch (40%) só se sustenta se o conteúdo for genuinamente absorvido.
