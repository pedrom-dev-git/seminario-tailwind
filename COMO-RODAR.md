# Como rodar — passo a passo

Dois caminhos. Para a **apresentação**, use o **Caminho A** (CDN, zero instalação).
O **Caminho B** (NPM na máquina) é o setup "de verdade" — cobre a seção *Instalação
via NPM* exigida no artigo e serve se quiserem mostrar o ambiente real.

> O enunciado aceita **CDN _ou_ NPM**. CDN já cumpre o requisito. NPM é bônus.

---

## Caminho A — CDN (recomendado para a aula, zero setup)

Não instala nada. Os arquivos já têm `<script src="...cdn...">` no `<head>`.

### Ato 1 — só Tailwind (o "problema")
1. Abrir o arquivo `aula-simples/index.html` num navegador
   (duplo clique, ou `xdg-open aula-simples/index.html`).
2. É HTML puro + Tailwind, **sem framework**. Repare: o card está **copiado 3×**
   com a mesma lista de classes → é a "poluição".

### Ato 2 — com framework (a "solução")
1. Abrir `index.html` (raiz) no navegador.
2. Mesmo visual, mas React: o card virou **componente** (escrito 1×) e a tela é
   **interativa** — digitar nome + "＋ Adicionar" cria card, "remover" tira.
3. **Redimensionar a janela**: o grid vai de 1 → 2 → 3 colunas (responsivo, sem
   escrever `@media`).

> Precisa de internet (a CDN baixa Tailwind/React na hora). Sem rede → ver
> "Plano B offline" no `pitch.md`.

---

## Caminho B — NPM na máquina (setup real)

Pré-requisitos: **Node.js 18+** instalado (`node --version`).

### B1 — Só Tailwind (sem framework)

```bash
# 1. cria um projeto Vite vazio
npm create vite@latest tailwind-puro -- --template vanilla
cd tailwind-puro

# 2. instala as dependências base
npm install

# 3. instala o Tailwind v4 + plugin do Vite
npm install tailwindcss @tailwindcss/vite
```

Edite **`vite.config.js`**:

```js
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [tailwindcss()],
})
```

Em **`src/style.css`** apague tudo e deixe **uma linha**:

```css
@import "tailwindcss";
```

Em `index.html` (do projeto Vite) use classes Tailwind normalmente, ex.:
`<h1 class="text-2xl font-bold text-indigo-600">Olá Tailwind</h1>`.

```bash
# 4. roda o servidor de desenvolvimento
npm run dev
```

Abra o endereço que aparecer (normalmente `http://localhost:5173`).

### B2 — Tailwind + React

```bash
npm create vite@latest tailwind-react -- --template react
cd tailwind-react
npm install
npm install tailwindcss @tailwindcss/vite
```

**`vite.config.js`** (mantém o plugin do React e adiciona o do Tailwind):

```js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [react(), tailwindcss()],
})
```

Em **`src/index.css`** deixe só:

```css
@import "tailwindcss";
```

Agora é só usar classes Tailwind nos componentes (`className="..."`).
Pode colar a lógica do nosso `index.html` (componente `Card`, `useState`).

```bash
npm run dev
```

> **Diferença CDN × NPM:** o CDN baixa o Tailwind inteiro e processa no navegador
> (ótimo p/ demo, lento p/ produção). O NPM/Vite gera **só o CSS das classes
> usadas** — bundle mínimo, é o jeito de produção. Mesma sintaxe de classe nos dois.

---

## O que tem que aparecer (verificação)

| | Esperado |
|---|---|
| Ato 1 (`aula-simples`) | 3 cards de produto, idênticos, sem botão de adicionar |
| Ato 2 (`index.html`) | campo + "＋ Adicionar", cards somem com "remover", grid 1→3 colunas ao redimensionar |
| NPM `npm run dev` | terminal mostra `Local: http://localhost:5173`; página estilizada |

## Problemas comuns

- **Página sem estilo nenhum (texto cru):** a CDN não carregou → sem internet, ou
  bloqueada. Teste a rede.
- **`npm: command not found`:** Node.js não instalado.
- **NPM: classes não aplicam:** faltou `@import "tailwindcss";` no CSS, ou o CSS
  não está sendo importado no `main.js`/`main.jsx`, ou o plugin não está no
  `vite.config.js`.
- **Porta 5173 ocupada:** o Vite sobe noutra porta — use a que ele imprimir.
