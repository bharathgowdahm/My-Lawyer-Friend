<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<meta name="description" content="My Lawyer Friend — plain-language explanations of Indian legal terms. Free, bilingual (English / ಕನ್ನಡ), no jargon." />
<meta name="theme-color" content="#070d1f" />
<title>My Lawyer Friend — Law Made Simple</title>

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />

<style>
/* ============ Design tokens ============ */
:root{
  --gold:#d4af37; --gold-hi:#f6e27a; --gold-lo:#c9962e;
  --navy-900:#070d1f; --navy-800:#0a1128; --navy-700:#0d1730; --navy-600:#131f42;
  --ink-100:#eef1f8; --ink-200:#e2e8f0; --ink-300:#cbd5e1; --ink-400:#94a3b8; --ink-500:#64748b;
  --amber-200:#fde68a; --amber-300:#fcd34d; --amber-400:#fbbf24; --amber-500:#f59e0b; --amber-600:#d97706;
  --red-400:#f87171; --red-500:#ef4444;
  --radius-sm:.5rem; --radius:.75rem; --radius-lg:1rem; --radius-xl:1.5rem; --radius-full:9999px;
  --shadow-lg:0 10px 15px -3px rgb(0 0 0/.35), 0 4px 6px -4px rgb(0 0 0/.25);
  --shadow-xl:0 20px 25px -5px rgb(0 0 0/.4), 0 8px 10px -6px rgb(0 0 0/.3);
  --shadow-2xl:0 25px 50px -12px rgb(0 0 0/.6);
  --glass-bg:linear-gradient(145deg,rgb(255 255 255/.07),rgb(255 255 255/.025));
  --glass-bd:1px solid rgb(212 175 55/.16);
  --glass-strong-bg:linear-gradient(145deg,rgb(20 30 60/.85),rgb(10 16 36/.92));
  --glass-strong-bd:1px solid rgb(212 175 55/.22);
  --ease:cubic-bezier(.22,1,.36,1);
  --header-h:64px;
  --safe-top:env(safe-area-inset-top,0px);
}

/* ============ Reset ============ */
*,*::before,*::after{box-sizing:border-box;border:0 solid}
html,body{margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:calc(var(--header-h) + var(--safe-top) + 16px);-webkit-text-size-adjust:100%}
body{
  font-family:Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  background:var(--navy-900);color:var(--ink-100);line-height:1.5;
  -webkit-font-smoothing:antialiased;overflow-x:clip;min-height:100dvh;
}
img,svg{display:block;max-width:100%}
button,input{font:inherit;color:inherit}
button{cursor:pointer;background:none;border:none;padding:0}
a{color:inherit;text-decoration:none}
ul,ol{list-style:none;margin:0;padding:0}
h1,h2,h3,h4,p{margin:0}
:focus-visible{outline:2px solid var(--amber-400);outline-offset:3px;border-radius:6px}

/* ============ Utilities ============ */
.container{width:100%;max-width:1280px;margin-inline:auto;padding-inline:clamp(1rem,4vw,1.5rem)}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.font-display{font-family:Fraunces,Georgia,serif}
.gold-text{
  background:linear-gradient(120deg,#f6e27a,#d4af37 35%,#f9eec3 55%,#c9962e 80%,#f6e27a);
  -webkit-background-clip:text;background-clip:text;color:transparent;
}
.glass{background:var(--glass-bg);border:var(--glass-bd);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px)}
.glass-strong{background:var(--glass-strong-bg);border:var(--glass-strong-bd);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px)}
.gold-ring:focus-within{border-color:rgb(212 175 55/.65);box-shadow:0 0 0 4px rgb(212 175 55/.15),0 18px 50px -18px rgb(212 175 55/.35)}

/* ============ Animations ============ */
@keyframes fadeUp{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:translateY(0)}}
@keyframes pulseDot{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(1.55);opacity:.5}}
@keyframes ticker{from{transform:translateX(0)}to{transform:translateX(-50%)}}
@keyframes floaty{0%,100%{transform:translateY(0)}50%{transform:translateY(-18px)}}
@keyframes spinIn{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}
.anim-up{animation:fadeUp .7s var(--ease) both}
.anim-up-1{animation:fadeUp .7s var(--ease) .08s both}
.anim-up-2{animation:fadeUp .7s var(--ease) .16s both}
.anim-up-3{animation:fadeUp .7s var(--ease) .24s both}
.panel-in{animation:spinIn .45s var(--ease) both}
.live-dot{animation:pulseDot 1.6s ease-in-out infinite}
.floaty{animation:floaty 9s ease-in-out infinite}
@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{animation-duration:.001ms!important;animation-iteration-count:1!important;transition-duration:.001ms!important;scroll-behavior:auto!important}
}

/* ============ Ticker ============ */
.ticker-bar{
  background:linear-gradient(90deg,var(--navy-700),var(--navy-600),var(--navy-700));
  border-bottom:1px solid rgb(251 191 36/.15);overflow:hidden;
}
.ticker-inner{display:flex;align-items:center}
.ticker-badge{
  flex-shrink:0;z-index:2;display:flex;align-items:center;gap:.5rem;
  padding:.55rem clamp(.75rem,3vw,1.25rem);
  background:linear-gradient(90deg,var(--amber-500),var(--amber-600));
  color:var(--navy-800);font-size:.6875rem;font-weight:700;
  text-transform:uppercase;letter-spacing:.1em;white-space:nowrap;
}
.ticker-badge .dot{width:.5rem;height:.5rem;border-radius:var(--radius-full);background:var(--navy-800)}
.ticker-viewport{flex:1;overflow:hidden;position:relative}
.ticker-track{display:flex;white-space:nowrap;padding:.5rem 0;width:max-content;animation:ticker 55s linear infinite}
.ticker-viewport:hover .ticker-track{animation-play-state:paused}
.ticker-item{margin:0 1.5rem;font-size:.75rem;color:var(--ink-300)}
.ticker-item .court{color:var(--amber-300);font-weight:600}
@media(min-width:640px){.ticker-item{font-size:.8125rem}}

/* ============ Header ============ */
.site-header{
  position:sticky;top:var(--safe-top);z-index:40;
  background:rgb(7 13 31/.82);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border-bottom:1px solid rgb(255 255 255/.05);
}
.header-row{display:flex;align-items:center;justify-content:space-between;height:var(--header-h);gap:.75rem}
.brand{
  display:flex;align-items:center;gap:.75rem;padding:.3rem .55rem;margin-left:-.55rem;
  border-radius:var(--radius);transition:background .25s,box-shadow .25s,transform .25s;text-align:left;
}
.brand:hover,.brand.is-pulsing{background:rgb(251 191 36/.1);box-shadow:0 0 0 1px rgb(251 191 36/.3)}
.brand.is-pulsing{background:rgb(251 191 36/.25);box-shadow:0 0 0 2px rgb(251 191 36/.7);transform:scale(1.04)}
.brand-mark{
  width:2.5rem;height:2.5rem;border-radius:var(--radius);flex-shrink:0;
  background:linear-gradient(135deg,var(--amber-300),var(--amber-600));
  display:grid;place-items:center;box-shadow:0 10px 15px -3px rgb(245 158 11/.25);
}
.brand-mark svg{width:1.25rem;height:1.25rem;color:var(--navy-800)}
.brand-name{display:block;font-family:Fraunces,serif;font-weight:700;font-size:1.0625rem;line-height:1.05}
.brand-tag{display:block;font-size:.5625rem;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-400);margin-top:.2rem}

.nav-desktop{display:none;align-items:center;gap:1.25rem;font-size:.875rem;font-weight:500}
@media(min-width:1024px){.nav-desktop{display:flex}}
.nav-link{padding:.4rem .8rem;border-radius:var(--radius-full);color:var(--ink-300);transition:color .2s,background .2s,box-shadow .2s}
.nav-link:hover{color:var(--amber-300)}
.nav-link.is-active{color:var(--amber-300);background:rgb(251 191 36/.1);box-shadow:0 0 0 1px rgb(251 191 36/.3)}

.header-actions{display:flex;align-items:center;gap:.5rem}
.lang-btn,.menu-btn{
  display:inline-flex;align-items:center;gap:.375rem;padding:.5rem .8rem;
  border-radius:var(--radius-full);border:var(--glass-bd);background:var(--glass-bg);
  color:var(--amber-200);font-size:.75rem;font-weight:600;transition:border-color .2s,background .2s;
}
.lang-btn:hover,.menu-btn:hover{border-color:rgb(251 191 36/.5);background:rgb(251 191 36/.08)}
.lang-btn svg,.menu-btn svg{width:.875rem;height:.875rem}
.menu-btn{padding:.55rem}
.menu-btn svg{width:1.15rem;height:1.15rem}
@media(min-width:1024px){.menu-btn{display:none}}

.nav-mobile{
  display:none;flex-direction:column;gap:.15rem;padding:.65rem 1rem .9rem;
  border-top:1px solid rgb(255 255 255/.05);background:rgb(10 17 40/.96);
}
.nav-mobile.is-open{display:flex;animation:fadeUp .25s var(--ease) both}
.nav-mobile .nav-link{width:100%;text-align:left;padding:.65rem .8rem}
@media(min-width:1024px){.nav-mobile{display:none!important}}

/* ============ Hero ============ */
.hero{position:relative;overflow:hidden;isolation:isolate}
.hero::before{
  content:"";position:absolute;inset:0;z-index:-2;
  background-image:linear-gradient(rgb(212 175 55/.055) 1px,transparent 1px),linear-gradient(90deg,rgb(212 175 55/.055) 1px,transparent 1px);
  background-size:44px 44px;
  -webkit-mask-image:radial-gradient(ellipse 90% 70% at 50% 30%,#000 30%,transparent 75%);
          mask-image:radial-gradient(ellipse 90% 70% at 50% 30%,#000 30%,transparent 75%);
}
.glow{position:absolute;border-radius:var(--radius-full);pointer-events:none;z-index:-1;filter:blur(120px)}
.glow-1{top:-8rem;left:50%;translate:-50% 0;width:min(720px,90vw);height:420px;background:rgb(245 158 11/.18)}
.glow-2{top:10rem;left:-6rem;width:18rem;height:18rem;background:rgb(79 70 229/.22)}
.glow-3{top:16rem;right:-6rem;width:18rem;height:18rem;background:rgb(251 191 36/.12)}

.hero-inner{max-width:64rem;margin-inline:auto;text-align:center;padding-block:clamp(3rem,10vw,6rem)}
.hero-badge{
  display:inline-flex;align-items:center;gap:.5rem;padding:.4rem 1rem;border-radius:var(--radius-full);
  border:var(--glass-bd);background:var(--glass-bg);
  color:var(--amber-200);font-size:.75rem;font-weight:500;margin-bottom:1.5rem;
}
.hero-badge svg{width:.9rem;height:.9rem}
@media(min-width:640px){.hero-badge{font-size:.875rem}}

.hero-title{font-weight:700;font-size:clamp(2.1rem,7vw,4.5rem);line-height:1.05;letter-spacing:-.025em}
.hero-sub{
  margin-top:clamp(1.1rem,3vw,1.5rem);color:rgb(203 213 225/.92);
  font-size:clamp(.9rem,2.2vw,1.125rem);max-width:42rem;margin-inline:auto;line-height:1.7;
}

.search-shell{margin-top:clamp(2rem,5vw,2.5rem);max-width:42rem;margin-inline:auto}
.search-box{
  display:flex;flex-direction:column;gap:.5rem;padding:.5rem;
  border-radius:var(--radius-lg);transition:border-color .2s,box-shadow .2s;
}
@media(min-width:640px){.search-box{flex-direction:row;border-radius:var(--radius-full)}}
.search-field{display:flex;align-items:center;flex:1;min-width:0;gap:.55rem;padding-inline:.75rem}
.search-field svg{width:1.15rem;height:1.15rem;color:var(--amber-300);flex-shrink:0}
.search-field input{
  width:100%;min-width:0;background:transparent;border:none;outline:none;
  padding:.65rem 0;font-size:.9rem;color:#fff;
}
.search-field input::placeholder{color:var(--ink-500)}
@media(min-width:640px){.search-field input{font-size:1rem}}
.search-actions{display:flex;gap:.5rem}
.btn{
  display:inline-flex;align-items:center;justify-content:center;gap:.45rem;
  padding:.65rem 1.25rem;border-radius:var(--radius);font-weight:700;font-size:.875rem;
  transition:filter .2s,transform .12s,background .2s,border-color .2s;
}
@media(min-width:640px){.btn{border-radius:var(--radius-full)}}
.btn:active{transform:scale(.96)}
.btn-gold{background:linear-gradient(90deg,var(--amber-400),var(--amber-600));color:var(--navy-800);box-shadow:0 10px 15px -3px rgb(245 158 11/.25)}
.btn-gold:hover{filter:brightness(1.08)}
.btn-ghost{border:var(--glass-bd);background:var(--glass-bg);color:var(--amber-200);font-weight:600}
.btn-ghost:hover{border-color:rgb(251 191 36/.55);background:rgb(251 191 36/.08)}
.btn svg{width:1rem;height:1rem}
.btn-search{flex:1;padding-inline:1.5rem}
@media(min-width:640px){.btn-search{flex:none}}

.popular-row{
  margin-top:1.25rem;display:flex;flex-wrap:wrap;align-items:center;justify-content:center;
  gap:.5rem;font-size:.75rem;
}
@media(min-width:640px){.popular-row{font-size:.875rem}}
.popular-label{color:var(--ink-400)}
.chip{
  padding:.4rem .8rem;border-radius:var(--radius-full);
  border:1px solid rgb(251 191 36/.25);color:rgb(253 230 138/.9);
  transition:background .2s,border-color .2s,color .2s;
}
.chip:hover{background:rgb(251 191 36/.1);border-color:rgb(251 191 36/.6);color:#fff}

.stat-row{margin-top:clamp(2.25rem,6vw,3.5rem);display:grid;grid-template-columns:repeat(3,1fr);gap:.75rem;max-width:36rem;margin-inline:auto}
.stat{padding:1rem .5rem;border-radius:var(--radius-lg);text-align:center;border:var(--glass-bd);background:var(--glass-bg)}
.stat-value{font-family:Fraunces,serif;font-weight:700;font-size:clamp(1.4rem,4vw,1.875rem)}
.stat-label{margin-top:.25rem;font-size:.625rem;color:var(--ink-400);line-height:1.35}
@media(min-width:640px){.stat-label{font-size:.75rem}}

.hero-divider{position:relative;height:1px;background:linear-gradient(90deg,transparent,rgb(251 191 36/.4),transparent)}

/* ============ Sections ============ */
.section{padding-block:clamp(3.5rem,9vw,5rem)}
.section-tinted{
  background:rgb(10 19 48/.6);
  border-top:1px solid rgb(255 255 255/.05);
  border-bottom:1px solid rgb(255 255 255/.05);
}
.section-head{text-align:center;margin-bottom:clamp(2rem,5vw,3rem)}
.kicker{
  display:inline-flex;align-items:center;gap:.5rem;
  color:var(--amber-300);font-size:.75rem;font-weight:700;
  text-transform:uppercase;letter-spacing:.2em;margin-bottom:.75rem;
}
.kicker svg{width:1rem;height:1rem}
.section-title{font-family:Fraunces,serif;font-weight:700;font-size:clamp(1.75rem,5vw,3rem);line-height:1.15;color:#fff}

/* ============ Category grid ============ */
.category-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.75rem}
@media(min-width:640px){.category-grid{gap:1.25rem}}
@media(min-width:1024px){.category-grid{grid-template-columns:repeat(3,minmax(0,1fr))}}

.category-card{
  position:relative;text-align:left;padding:1.1rem;border-radius:var(--radius-lg);
  border:var(--glass-bd);background:var(--glass-bg);
  transition:transform .3s var(--ease),border-color .3s,background .3s,box-shadow .3s;
}
@media(min-width:640px){.category-card{padding:1.75rem;border-radius:var(--radius-xl)}}
.category-card:hover{transform:translateY(-4px);border-color:rgb(251 191 36/.5)}
.category-card.is-active{
  background:linear-gradient(135deg,rgb(251 191 36/.22),rgb(217 119 6/.08));
  border-color:rgb(251 191 36/.65);box-shadow:0 20px 30px -12px rgb(245 158 11/.2);
}
.cat-icon{
  width:2.75rem;height:2.75rem;border-radius:var(--radius);
  display:grid;place-items:center;margin-bottom:.75rem;
  background:rgb(251 191 36/.1);border:1px solid rgb(251 191 36/.25);
  transition:background .3s,transform .3s;
}
.category-card:hover .cat-icon{background:rgb(251 191 36/.2)}
.category-card.is-active .cat-icon{background:linear-gradient(135deg,var(--amber-300),var(--amber-600));border-color:transparent}
@media(min-width:640px){.cat-icon{width:3.5rem;height:3.5rem;margin-bottom:1rem}}
.cat-icon svg{width:1.25rem;height:1.25rem;color:var(--amber-300)}
.category-card.is-active .cat-icon svg{color:var(--navy-800)}
@media(min-width:640px){.cat-icon svg{width:1.5rem;height:1.5rem}}
.cat-title{font-family:Fraunces,serif;font-weight:700;font-size:1rem;color:#fff}
@media(min-width:640px){.cat-title{font-size:1.25rem}}
.cat-sub{margin-top:.25rem;font-size:.6875rem;color:var(--ink-400);line-height:1.35}
@media(min-width:640px){.cat-sub{font-size:.875rem}}
.cat-count{margin-top:.5rem;font-size:.625rem;font-weight:600;color:rgb(252 211 77/.85)}
@media(min-width:640px){.cat-count{font-size:.75rem}}

/* ============ Term grid ============ */
.term-grid{display:grid;grid-template-columns:1fr;gap:1rem;margin-top:2rem}
@media(min-width:640px){.term-grid{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1024px){.term-grid{grid-template-columns:repeat(3,1fr)}}
.term-card{
  text-align:left;padding:1.25rem;border-radius:var(--radius-lg);
  border:var(--glass-bd);background:var(--glass-bg);
  transition:transform .25s,border-color .25s,background .25s;
  display:flex;flex-direction:column;gap:.4rem;
}
.term-card:hover{transform:translateY(-3px);border-color:rgb(251 191 36/.55);background:rgb(255 255 255/.05)}
.term-card h3{font-size:.9375rem;font-weight:600;color:#fff;line-height:1.35}
@media(min-width:640px){.term-card h3{font-size:1rem}}
.term-card p{
  font-size:.78rem;color:var(--ink-400);line-height:1.55;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;
}
.term-card .term-cta{
  display:inline-flex;align-items:center;gap:.3rem;margin-top:.5rem;
  color:var(--amber-300);font-size:.75rem;font-weight:700;
}
.term-card .term-cta svg{width:.85rem;height:.85rem;transition:transform .2s}
.term-card:hover .term-cta svg{transform:translateX(3px)}

/* ============ Explainer ============ */
.explainer-wrap{max-width:56rem;margin-inline:auto}
.explainer-empty{
  padding:clamp(2rem,6vw,2.5rem);border-radius:var(--radius-xl);
  border:var(--glass-bd);background:var(--glass-bg);text-align:center;
}
.explainer-empty svg{width:2.5rem;height:2.5rem;color:rgb(252 211 77/.7);margin:0 auto 1rem}
.explainer-empty p{color:var(--ink-300);font-size:.9rem;line-height:1.7}
@media(min-width:640px){.explainer-empty p{font-size:1rem}}

.notfound{
  padding:clamp(2rem,6vw,3rem);border-radius:var(--radius-xl);
  border:var(--glass-bd);background:var(--glass-bg);text-align:center;max-width:42rem;margin-inline:auto;
}
.notfound .alert-icon{
  width:3.5rem;height:3.5rem;border-radius:var(--radius-lg);margin:0 auto 1.25rem;
  background:rgb(251 191 36/.1);border:1px solid rgb(251 191 36/.3);
  display:grid;place-items:center;
}
.notfound .alert-icon svg{width:1.75rem;height:1.75rem;color:var(--amber-300)}
.notfound h3{font-family:Fraunces,serif;font-weight:700;font-size:1.5rem;color:#fff;margin-bottom:.5rem}
.notfound p{color:var(--ink-400);font-size:.9rem;margin-bottom:1.5rem}
.notfound .chip{margin:.15rem}
.notfound .chip-row{display:flex;flex-wrap:wrap;justify-content:center;gap:.5rem;margin-bottom:1.75rem}

.term-panel{
  border-radius:var(--radius-xl);overflow:hidden;box-shadow:var(--shadow-2xl);
  background:var(--glass-strong-bg);border:var(--glass-strong-bd);
  backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);
}
.panel-head{
  padding:clamp(1.5rem,4vw,2rem) clamp(1.5rem,4vw,2.5rem);
  background:linear-gradient(90deg,rgb(251 191 36/.2),rgb(245 158 11/.1),transparent);
  border-bottom:1px solid rgb(251 191 36/.2);
}
.panel-kicker{
  display:flex;align-items:center;gap:.5rem;
  color:var(--amber-300);font-size:.75rem;font-weight:700;
  text-transform:uppercase;letter-spacing:.18em;margin-bottom:.5rem;
}
.panel-kicker svg{width:.9rem;height:.9rem}
.panel-title{font-family:Fraunces,serif;font-weight:700;font-size:clamp(1.5rem,4.5vw,2.25rem);color:#fff;line-height:1.15}
.panel-body{padding:clamp(1.5rem,4vw,2.5rem)}
.panel-section{margin-bottom:1.75rem}
.panel-section:last-child{margin-bottom:0}
.panel-label{
  display:flex;align-items:center;gap:.5rem;
  color:var(--amber-200);font-weight:700;font-size:.75rem;
  text-transform:uppercase;letter-spacing:.06em;margin-bottom:.75rem;
}
.panel-label svg{width:1rem;height:1rem}
.panel-text{color:rgb(226 232 240/.95);font-size:.9rem;line-height:1.75}
@media(min-width:640px){.panel-text{font-size:.98rem}}

.step-list{display:flex;flex-direction:column;gap:.75rem}
.step{display:flex;gap:.85rem;align-items:flex-start}
.step-num{
  flex-shrink:0;width:1.75rem;height:1.75rem;border-radius:var(--radius-full);
  background:linear-gradient(135deg,var(--amber-300),var(--amber-600));
  color:var(--navy-800);font-size:.75rem;font-weight:700;
  display:grid;place-items:center;margin-top:.15rem;
}
.step-text{color:var(--ink-300);font-size:.875rem;line-height:1.65;padding-top:.2rem}
@media(min-width:640px){.step-text{font-size:.9375rem}}

.info-grid{display:grid;gap:.75rem;margin-bottom:1.75rem}
@media(min-width:640px){.info-grid{grid-template-columns:1fr 1fr;gap:1rem}}
.info-box{
  border:1px solid rgb(251 191 36/.2);background:rgb(251 191 36/.06);
  border-radius:var(--radius-lg);padding:1rem 1.25rem;
}
.info-box .panel-label{margin-bottom:.5rem}
.info-box .value{color:#fff;font-size:.875rem;font-weight:500;line-height:1.6}
@media(min-width:640px){.info-box .value{font-size:.9375rem}}

/* ============ News ============ */
.news-grid{display:grid;gap:1rem}
@media(min-width:640px){.news-grid{grid-template-columns:1fr 1fr}}
.news-card{
  position:relative;padding:1.25rem;border-radius:var(--radius-lg);
  border:var(--glass-bd);background:var(--glass-bg);
  transition:border-color .25s,transform .25s;
  animation:fadeUp .5s var(--ease) both;
}
.news-card:hover{border-color:rgb(251 191 36/.5);transform:translateY(-2px)}
.news-live{
  position:absolute;top:1rem;right:1rem;
  display:inline-flex;align-items:center;gap:.35rem;
  padding:.22rem .6rem;border-radius:var(--radius-full);
  background:rgb(239 68 68/.15);border:1px solid rgb(239 68 68/.4);
  color:var(--red-400);font-size:.625rem;font-weight:700;
  text-transform:uppercase;letter-spacing:.06em;
}
.news-live .dot{width:.375rem;height:.375rem;border-radius:var(--radius-full);background:var(--red-500)}
.news-court{
  display:flex;align-items:center;gap:.4rem;
  color:rgb(252 211 77/.9);font-size:.6875rem;font-weight:700;
  text-transform:uppercase;letter-spacing:.14em;margin-bottom:.6rem;
}
.news-court svg{width:.85rem;height:.85rem}
.news-title{font-size:.9rem;font-weight:600;color:#fff;line-height:1.4;margin-bottom:.4rem;padding-right:3rem}
@media(min-width:640px){.news-title{font-size:.9375rem}}
.news-detail{font-size:.78rem;color:var(--ink-400);line-height:1.55;margin-bottom:.6rem}
.news-time{display:flex;align-items:center;gap:.35rem;font-size:.6875rem;color:var(--ink-500)}
.news-time svg{width:.75rem;height:.75rem}

/* ============ Google ============ */
.google-wrap{position:relative;overflow:hidden}
.google-glow{position:absolute;top:0;right:0;width:24rem;height:24rem;background:rgb(245 158 11/.1);filter:blur(120px);border-radius:var(--radius-full);pointer-events:none}
.google-inner{position:relative;max-width:48rem;margin-inline:auto;text-align:center}
.google-sub{color:var(--ink-400);font-size:.9rem;max-width:36rem;margin:.75rem auto 2rem;line-height:1.7}
@media(min-width:640px){.google-sub{font-size:1rem}}
.google-form{
  display:flex;flex-direction:column;gap:.5rem;padding:.5rem;
  border-radius:var(--radius-lg);max-width:36rem;margin-inline:auto;
  transition:border-color .2s,box-shadow .2s;
}
@media(min-width:640px){.google-form{flex-direction:row;border-radius:var(--radius-xl)}}
.google-field{display:flex;align-items:center;flex:1;gap:.65rem;padding-inline:1rem}
.google-field .g-mark{font-family:Fraunces,serif;font-weight:700;font-size:1.125rem;color:#fff;user-select:none}
.google-field input{flex:1;min-width:0;background:transparent;border:none;outline:none;padding:.75rem 0;font-size:.9rem;color:#fff}
@media(min-width:640px){.google-field input{font-size:1rem}}
.google-note{margin-top:1rem;font-size:.6875rem;color:var(--ink-500)}

/* ============ Links ============ */
.links-grid{display:grid;gap:1rem}
@media(min-width:640px){.links-grid{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1024px){.links-grid{grid-template-columns:repeat(4,1fr)}}
.link-card{
  display:flex;flex-direction:column;padding:1.5rem;border-radius:var(--radius-xl);
  border:var(--glass-bd);background:var(--glass-bg);
  transition:transform .3s var(--ease),border-color .3s,background .3s;
}
.link-card:hover{transform:translateY(-6px);border-color:rgb(251 191 36/.55);background:rgb(255 255 255/.05)}
.link-icon{
  width:3rem;height:3rem;border-radius:var(--radius-lg);margin-bottom:1.25rem;
  background:linear-gradient(135deg,var(--amber-300),var(--amber-600));
  display:grid;place-items:center;box-shadow:0 10px 15px -3px rgb(245 158 11/.2);
  transition:transform .3s;
}
.link-card:hover .link-icon{transform:scale(1.08)}
.link-icon svg{width:1.5rem;height:1.5rem;color:var(--navy-800)}
.link-name{font-family:Fraunces,serif;font-weight:700;font-size:1.0625rem;color:#fff;margin-bottom:.5rem}
.link-desc{font-size:.78rem;color:var(--ink-400);line-height:1.6;flex:1}
@media(min-width:640px){.link-desc{font-size:.875rem}}
.link-cta{
  display:inline-flex;align-items:center;gap:.35rem;margin-top:1.25rem;
  color:var(--amber-300);font-size:.85rem;font-weight:700;
}
.link-cta svg{width:1rem;height:1rem;transition:transform .25s}
.link-card:hover .link-cta svg{transform:translate(.15rem,-.15rem)}

/* ============ Footer ============ */
.site-footer{border-top:1px solid rgb(251 191 36/.15);background:#050a1a}
.footer-top{
  display:flex;flex-direction:column;align-items:center;justify-content:space-between;
  gap:1.5rem;margin-bottom:2rem;
}
@media(min-width:640px){.footer-top{flex-direction:row}}
.footer-brand{display:flex;align-items:center;gap:.75rem}
.footer-brand .brand-mark{width:2.5rem;height:2.5rem;border-radius:var(--radius)}
.footer-brand .brand-mark svg{width:1.25rem;height:1.25rem}
.footer-tagline{display:flex;align-items:center;gap:.5rem;font-size:.75rem;color:var(--ink-500)}
.footer-tagline svg{width:1rem;height:1rem;color:var(--amber-300)}
.disclaimer{
  display:flex;gap:.75rem;padding:1rem 1.25rem;border-radius:var(--radius-lg);
  border:1px solid rgb(251 191 36/.2);background:rgb(251 191 36/.05);
}
.disclaimer svg{width:1.15rem;height:1.15rem;color:var(--amber-300);flex-shrink:0;margin-top:.15rem}
.disclaimer p{font-size:.75rem;color:rgb(253 230 138/.85);line-height:1.7}
@media(min-width:640px){.disclaimer p{font-size:.875rem}}
.disclaimer strong{color:var(--amber-200);font-weight:700}
.copyright{text-align:center;font-size:.6875rem;color:#475569;margin-top:2rem}

/* ============ Scrollbar ============ */
::-webkit-scrollbar{width:10px;height:10px}
::-webkit-scrollbar-track{background:var(--navy-900)}
::-webkit-scrollbar-thumb{background:#2a3358;border-radius:8px;border:2px solid var(--navy-900)}
::-webkit-scrollbar-thumb:hover{background:var(--gold)}
::selection{background:rgb(212 175 55/.35);color:#fff}
</style>
</head>

<body>

<!-- ============ SVG sprite ============ -->
<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <defs>
    <symbol id="i-scale" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/>
      <path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>
    </symbol>
    <symbol id="i-shield" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>
      <path d="M12 8v4"/><path d="M12 16h.01"/>
    </symbol>
    <symbol id="i-file" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/>
      <path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>
    </symbol>
    <symbol id="i-users" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>
      <path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>
    </symbol>
    <symbol id="i-home" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/>
      <path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
    </symbol>
    <symbol id="i-cpu" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/>
      <path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/>
      <path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/>
    </symbol>
    <symbol id="i-bag" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/>
      <path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>
    </symbol>
    <symbol id="i-landmark" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <line x1="3" x2="21" y1="22" y2="22"/><line x1="6" x2="6" y1="18" y2="11"/>
      <line x1="10" x2="10" y1="18" y2="11"/><line x1="14" x2="14" y1="18" y2="11"/>
      <line x1="18" x2="18" y1="18" y2="11"/><polygon points="12 2 20 7 4 7"/>
    </symbol>
    <symbol id="i-book" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 7v14"/>
      <path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/>
    </symbol>
    <symbol id="i-heart" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>
      <path d="M12 5 9.04 7.96a2.17 2.17 0 0 0 0 3.08c.82.82 2.13.85 3 .07l2.07-1.9a2.82 2.82 0 0 1 3.79 0l2.96 2.66"/>
      <path d="m18 15-2-2"/><path d="m15 18-2-2"/>
    </symbol>
    <symbol id="i-sparkles" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z"/>
      <path d="M20 3v4"/><path d="M22 5h-4"/><path d="M4 17v2"/><path d="M5 18H3"/>
    </symbol>
    <symbol id="i-alert" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/>
      <path d="M12 9v4"/><path d="M12 17h.01"/>
    </symbol>
    <symbol id="i-clock" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
    </symbol>
    <symbol id="i-rupee" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M6 3h12"/><path d="M6 8h12"/><path d="m6 13 8.5 8"/><path d="M6 13h3"/>
      <path d="M9 13c6.667 0 6.667-10 0-10"/>
    </symbol>
    <symbol id="i-search" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>
    </symbol>
    <symbol id="i-globe" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>
    </symbol>
    <symbol id="i-arrow-right" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>
    </symbol>
    <symbol id="i-chevron-right" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="m9 18 6-6-6-6"/>
    </symbol>
    <symbol id="i-languages" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/>
      <path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/>
    </symbol>
    <symbol id="i-list" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="m3 17 2 2 4-4"/><path d="m3 7 2 2 4-4"/><path d="M13 6h8"/><path d="M13 12h8"/><path d="M13 18h8"/>
    </symbol>
    <symbol id="i-badge" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z"/>
      <path d="m9 12 2 2 4-4"/>
    </symbol>
    <symbol id="i-external" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M15 3h6v6"/><path d="M10 14 21 3"/>
      <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
    </symbol>
    <symbol id="i-menu" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/>
    </symbol>
    <symbol id="i-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M18 6 6 18"/><path d="m6 6 12 12"/>
    </symbol>
    <symbol id="i-zap" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"/>
    </symbol>
    <symbol id="i-gavel" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="m14.5 12.5-8 8a2.119 2.119 0 1 1-3-3l8-8"/><path d="m16 16 6-6"/>
      <path d="m8 8 6-6"/><path d="m9 7 8 8"/><path d="m21 11-8-8"/>
    </symbol>
  </defs>
</svg>

<!-- ============ App root ============ -->
<div id="app"></div>

<script>
(() => {
  "use strict";

  /* =========================================================
     DATA
     ========================================================= */

  const CATEGORIES = [
    { id:"criminal",  en:"Criminal",    kn:"ಕ್ರಿಮಿನಲ್",     tagEn:"FIR, bail, warrants & police matters",       tagKn:"FIR, ಜಾಮೀನು, ವಾರಂಟ್ ಮತ್ತು ಪೊಲೀಸ್ ವಿಷಯಗಳು",       icon:"i-shield" },
    { id:"civil",     en:"Civil",       kn:"ಸಿವಿಲ್",        tagEn:"Money recovery, cheques & court suits",      tagKn:"ಹಣ ವಸೂಲಿ, ಚೆಕ್ ಮತ್ತು ನ್ಯಾಯಾಲಯದ ದಾವೆಗಳು",         icon:"i-file" },
    { id:"family",    en:"Family",      kn:"ಕುಟುಂಬ",        tagEn:"Divorce, custody & maintenance",              tagKn:"ವಿಚ್ಛೇದನ, ಪಾಲನೆ ಮತ್ತು ಜೀವನಾಂಶ",                 icon:"i-users" },
    { id:"property",  en:"Property",    kn:"ಆಸ್ತಿ",         tagEn:"Land disputes, tenancy & registration",       tagKn:"ಭೂ ವಿವಾದ, ಬಾಡಿಗೆ ಮತ್ತು ನೋಂದಣಿ",                  icon:"i-home" },
    { id:"cyber",     en:"Cyber Crime", kn:"ಸೈಬರ್ ಅಪರಾಧ",  tagEn:"Online fraud, hacking & reporting",           tagKn:"ಆನ್‌ಲೈನ್ ವಂಚನೆ, ಹ್ಯಾಕಿಂಗ್ ಮತ್ತು ದೂರು",           icon:"i-cpu" },
    { id:"consumer",  en:"Consumer",    kn:"ಗ್ರಾಹಕ",        tagEn:"Refunds, defects & e-Daakhil complaints",     tagKn:"ಮರುಪಾವತಿ, ದೋಷಗಳು ಮತ್ತು ಇ-ದಾಖಿಲ್ ದೂರುಗಳು",          icon:"i-bag" }
  ];

  const TERMS = [
    {
      id:"fir", category:"criminal",
      en:"FIR (First Information Report)", kn:"FIR (ಪ್ರಥಮ ಮಾಹಿತಿ ವರದಿ)",
      keywords:["fir","first information report","police complaint","complaint","police","report crime"],
      meaningEn:"An FIR is the written record the police make when you report a serious (cognizable) crime like theft, assault or fraud. Once registered, the police must investigate. You are entitled to a free copy, and the FIR gets a number you can track online.",
      meaningKn:"ಕಳ್ಳತನ, ಹಲ್ಲೆ ಅಥವಾ ವಂಚನೆಯಂತಹ ಗಂಭೀರ ಅಪರಾಧವನ್ನು ನೀವು ವರದಿ ಮಾಡಿದಾಗ ಪೊಲೀಸರು ಮಾಡುವ ಲಿಖಿತ ದಾಖಲೆಯೇ FIR. ನೋಂದಣಿಯಾದ ನಂತರ ಪೊಲೀಸರು ತನಿಖೆ ನಡೆಸಬೇಕು. ನಿಮಗೆ ಉಚಿತ ಪ್ರತಿಯ ಹಕ್ಕಿದೆ ಮತ್ತು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಟ್ರ್ಯಾಕ್ ಮಾಡಬಹುದಾದ ಸಂಖ್ಯೆ ಸಿಗುತ್ತದೆ.",
      steps:["Go to the nearest police station (or use your state's online citizen portal)","Give your complaint in writing, or dictate it — the officer must write it down","Read it carefully, sign it, and take your free signed copy with the FIR number","The police begin investigation and file a chargesheet in court"],
      timeEn:"Registered the same day · Investigation usually 60–90 days", timeKn:"ಅದೇ ದಿನ ನೋಂದಣಿ · ತನಿಖೆ ಸಾಮಾನ್ಯವಾಗಿ 60–90 ದಿನಗಳು",
      costEn:"Completely free — no fee to file an FIR", costKn:"ಸಂಪೂರ್ಣ ಉಚಿತ — FIR ದಾಖಲಿಸಲು ಯಾವುದೇ ಶುಲ್ಕವಿಲ್ಲ"
    },
    {
      id:"bail", category:"criminal",
      en:"Bail", kn:"ಜಾಮೀನು",
      keywords:["bail","jamin","bail application","release","regular bail","station bail","surety"],
      meaningEn:"Bail is the court's permission for an arrested person to stay out of jail while the trial continues. The court usually asks for a surety (a person who guarantees you) and a bond amount, which is refunded after the trial if you attend all hearings.",
      meaningKn:"ವಿಚಾರಣೆ ಮುಂದುವರಿದಿರುವಾಗ ಬಂಧಿತ ವ್ಯಕ್ತಿ ಜೈಲಿನ ಹೊರಗೆ ಇರಲು ನ್ಯಾಯಾಲಯ ನೀಡುವ ಅನುಮತಿಯೇ ಜಾಮೀನು. ನ್ಯಾಯಾಲಯ ಸಾಮಾನ್ಯವಾಗಿ ಜಾಮೀನುದಾರ ಮತ್ತು ಬಾಂಡ್ ಮೊತ್ತವನ್ನು ಕೇಳುತ್ತದೆ; ಎಲ್ಲಾ ವಿಚಾರಣೆಗಳಿಗೆ ಹಾಜರಾದರೆ ವಿಚಾರಣೆಯ ನಂತರ ಮೊತ್ತ ಮರಳಿ ಸಿಗುತ್ತದೆ.",
      steps:["A lawyer files a bail application in the concerned court","The court hears arguments from both sides","The judge sets conditions — surety, bond amount, passport surrender etc.","Deposit the bond and complete surety formalities","The accused is released from custody"],
      timeEn:"Station bail: same day · Regular bail: 1 day – 2 weeks", timeKn:"ಠಾಣಾ ಜಾಮೀನು: ಅದೇ ದಿನ · ಸಾಮಾನ್ಯ ಜಾಮೀನು: 1 ದಿನ – 2 ವಾರಗಳು",
      costEn:"Lawyer fees ₹5,000 – ₹50,000+ · Bond amount is refunded after trial", costKn:"ವಕೀಲರ ಶುಲ್ಕ ₹5,000 – ₹50,000+ · ವಿಚಾರಣೆಯ ನಂತರ ಬಾಂಡ್ ಮೊತ್ತ ಮರಳುತ್ತದೆ"
    },
    {
      id:"anticipatory-bail", category:"criminal",
      en:"Anticipatory Bail", kn:"ಮುಂಗಡ ಜಾಮೀನು",
      keywords:["anticipatory","advance bail","pre arrest","438"],
      meaningEn:"Anticipatory bail is protection from arrest before it happens — you ask the court in advance that if the police come to arrest you, you should be released on bail immediately. It is filed in the Sessions Court or High Court.",
      meaningKn:"ಬಂಧನವಾಗುವ ಮೊದಲೇ ಪಡೆಯುವ ರಕ್ಷಣೆಯೇ ಮುಂಗಡ ಜಾಮೀನು — ಪೊಲೀಸರು ಬಂಧಿಸಲು ಬಂದರೆ ತಕ್ಷಣ ಜಾಮೀನಿನಲ್ಲಿ ಬಿಡುಗಡೆ ಮಾಡಬೇಕೆಂದು ನ್ಯಾಯಾಲಯವನ್ನು ಮುಂಚಿತವಾಗಿ ಕೇಳುವುದು.",
      steps:["Lawyer files the application in the Sessions Court or High Court","Court may grant interim protection from arrest","Notice is issued to the police / prosecution for their reply","After hearing, the court grants bail with conditions","Surrender before the court or investigating officer as directed"],
      timeEn:"Usually 1 – 4 weeks", timeKn:"ಸಾಮಾನ್ಯವಾಗಿ 1 – 4 ವಾರಗಳು",
      costEn:"Lawyer fees ₹15,000 – ₹1,00,000+", costKn:"ವಕೀಲರ ಶುಲ್ಕ ₹15,000 – ₹1,00,000+"
    },
    {
      id:"summons", category:"criminal",
      en:"Court Summons", kn:"ನ್ಯಾಯಾಲಯದ ಸಮನ್ಸ್",
      keywords:["summons","court notice","notice","summon"],
      meaningEn:"A summons is a court order asking you to appear before it on a fixed date — as a witness, accused or party to a case. Ignoring a summons can lead to a warrant, so always note the date and respond.",
      meaningKn:"ಸಾಕ್ಷಿ, ಆರೋಪಿ ಅಥವಾ ಪ್ರಕರಣದ ಪಕ್ಷವಾಗಿ ನಿಗದಿತ ದಿನಾಂಕದಂದು ಹಾಜರಾಗುವಂತೆ ಕೇಳುವ ನ್ಯಾಯಾಲಯದ ಆದೇಶವೇ ಸಮನ್ಸ್. ಸಮನ್ಸ್ ಅನ್ನು ನಿರ್ಲಕ್ಷಿಸಿದರೆ ವಾರಂಟ್ ಬರಬಹುದು, ಆದ್ದರಿಂದ ದಿನಾಂಕವನ್ನು ಗಮನಿಸಿ ಪ್ರತಿಕ್ರಿಯಿಸಿ.",
      steps:["Receive the summons and note the date, time and court room","Appear in person, or send your lawyer if permitted","Carry an ID and any documents mentioned","Follow the judge's directions on the next date"],
      timeEn:"Arrives within days of issue · Attend on the date given", timeKn:"ಜಾರಿಯಾದ ಕೆಲವು ದಿನಗಳಲ್ಲಿ ಬರುತ್ತದೆ · ನೀಡಿದ ದಿನಾಂಕದಂದು ಹಾಜರಾಗಿ",
      costEn:"No fee to receive · Lawyer fees only if you hire one", costKn:"ಸ್ವೀಕರಿಸಲು ಶುಲ್ಕವಿಲ್ಲ · ವಕೀಲರನ್ನು ನೇಮಿಸಿದರೆ ಮಾತ್ರ ಶುಲ್ಕ"
    },
    {
      id:"arrest-warrant", category:"criminal",
      en:"Arrest Warrant", kn:"ಬಂಧನ ವಾರಂಟ್",
      keywords:["warrant","arrest warrant","non bailable warrant","nbw"],
      meaningEn:"An arrest warrant is a judge's written order authorising the police to arrest a person and bring them to court — usually issued when someone ignores summons or is evading the case. A bailable warrant lets you get bail at the police station; a non-bailable one means you must go before the judge.",
      meaningKn:"ವ್ಯಕ್ತಿಯನ್ನು ಬಂಧಿಸಿ ನ್ಯಾಯಾಲಯಕ್ಕೆ ಹಾಜರುಪಡಿಸಲು ಪೊಲೀಸರಿಗೆ ಅಧಿಕಾರ ನೀಡುವ ನ್ಯಾಯಾಧೀಶರ ಲಿಖಿತ ಆದೇಶವೇ ಬಂಧನ ವಾರಂಟ್.",
      steps:["Warrant is issued by the magistrate / judge","Police execute it and arrest the person","The person must be produced before a magistrate within 24 hours","Bail or remand hearing happens immediately"],
      timeEn:"Can be executed any time after it is issued", timeKn:"ಜಾರಿಯಾದ ನಂತರ ಯಾವುದೇ ಸಮಯದಲ್ಲಿ ಜಾರಿಗೊಳಿಸಬಹುದು",
      costEn:"Lawyer fees ₹10,000+ to seek recall / cancellation", costKn:"ರದ್ದತಿ / ಹಿಂಪಡೆಯಲು ವಕೀಲರ ಶುಲ್ಕ ₹10,000+"
    },
    {
      id:"cheque-bounce", category:"civil",
      en:"Cheque Bounce (Section 138)", kn:"ಚೆಕ್ ಬೌನ್ಸ್ (ಸೆಕ್ಷನ್ 138)",
      keywords:["cheque bounce","138","ni act","bounced cheque","check bounce"],
      meaningEn:"When a cheque bounces due to insufficient funds, it is a criminal offence under Section 138 of the Negotiable Instruments Act. The payee can send a legal notice and, if unpaid, file a criminal complaint — punishable with up to 2 years in jail or a fine.",
      meaningKn:"ಸಾಕಷ್ಟು ಹಣವಿಲ್ಲದೆ ಚೆಕ್ ಬೌನ್ಸ್ ಆದರೆ, ನೆಗೋಷಿಯಬಲ್ ಇನ್‌ಸ್ಟ್ರುಮೆಂಟ್ಸ್ ಕಾಯ್ದೆಯ ಸೆಕ್ಷನ್ 138 ರ ಅಡಿಯಲ್ಲಿ ಅದು ಕ್ರಿಮಿನಲ್ ಅಪರಾಧ.",
      steps:["Send a written demand notice within 30 days of the bounce","Give the drawer 15 days to pay after receiving the notice","If unpaid, file a complaint in court within the next 30 days","Trial proceeds — most cases settle with payment + compensation"],
      timeEn:"Typically 6 months – 2 years", timeKn:"ಸಾಮಾನ್ಯವಾಗಿ 6 ತಿಂಗಳು – 2 ವರ್ಷಗಳು",
      costEn:"Lawyer fees ₹10,000 – ₹50,000+", costKn:"ವಕೀಲರ ಶುಲ್ಕ ₹10,000 – ₹50,000+"
    },
    {
      id:"money-recovery", category:"civil",
      en:"Money Recovery Suit", kn:"ಹಣ ವಸೂಲಿ ದಾವೆ",
      keywords:["money recovery","civil suit","loan recovery","debt","recovery suit"],
      meaningEn:"If someone owes you money and refuses to pay, you can file a civil suit for recovery in court. You need proof — loan agreement, bank transfers, messages or witnesses. The court can order payment with interest and attach the debtor's property if they don't comply.",
      meaningKn:"ಯಾರಾದರೂ ನಿಮಗೆ ಹಣ ಕೊಡಬೇಕಿದ್ದು ಪಾವತಿಸಲು ನಿರಾಕರಿಸಿದರೆ, ನ್ಯಾಯಾಲಯದಲ್ಲಿ ಹಣ ವಸೂಲಿಗಾಗಿ ಸಿವಿಲ್ ದಾವೆ ಹೂಡಬಹುದು.",
      steps:["Send a legal notice demanding payment within a deadline","File the suit in the civil court with all proof attached","Both sides present evidence and arguments","Court passes a judgment (decree) for payment","If unpaid, enforce the decree — property can be attached"],
      timeEn:"Usually 1 – 3 years", timeKn:"ಸಾಮಾನ್ಯವಾಗಿ 1 – 3 ವರ್ಷಗಳು",
      costEn:"Court fee based on claim amount + lawyer fees", costKn:"ಹಕ್ಕು ಮೊತ್ತದ ಆಧಾರದ ಮೇಲೆ ನ್ಯಾಯಾಲಯ ಶುಲ್ಕ + ವಕೀಲರ ಶುಲ್ಕ"
    },
    {
      id:"divorce", category:"family",
      en:"Divorce", kn:"ವಿಚ್ಛೇದನ",
      keywords:["divorce","talaq","mutual divorce","separation","divorce process"],
      meaningEn:"Divorce is the legal end of a marriage granted by a family court. Mutual-consent divorce (both partners agree) is faster and simpler; a contested divorce (one side disagrees) takes longer. The court also settles alimony, child custody and property division.",
      meaningKn:"ಕುಟುಂಬ ನ್ಯಾಯಾಲಯ ನೀಡುವ ಮದುವೆಯ ಕಾನೂನುಬದ್ಧ ಅಂತ್ಯವೇ ವಿಚ್ಛೇದನ. ಪರಸ್ಪರ ಒಪ್ಪಿಗೆಯ ವಿಚ್ಛೇದನ ವೇಗ ಮತ್ತು ಸರಳ; ವಿವಾದಿತ ವಿಚ್ಛೇದನ ಹೆಚ್ಚು ಸಮಯ ತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ.",
      steps:["File a divorce petition (joint for mutual, single for contested)","Attend court counselling / mediation sessions","Mutual cases have a cooling period (often waived by courts now)","Agree on alimony, custody and property terms","Court grants the divorce decree"],
      timeEn:"Mutual: 6 – 12 months · Contested: 2 – 5 years", timeKn:"ಪರಸ್ಪರ: 6 – 12 ತಿಂಗಳು · ವಿವಾದಿತ: 2 – 5 ವರ್ಷಗಳು",
      costEn:"₹25,000 – ₹2,00,000+ depending on complexity", costKn:"ಸಂಕೀರ್ಣತೆಯನ್ನು ಅವಲಂಬಿಸಿ ₹25,000 – ₹2,00,000+"
    },
    {
      id:"alimony", category:"family",
      en:"Alimony / Maintenance", kn:"ಜೀವನಾಂಶ / ನಿರ್ವಹಣಾ ಭತ್ಯೆ",
      keywords:["alimony","maintenance","monthly maintenance","125 crpc","spouse support"],
      meaningEn:"Alimony (maintenance) is financial support a court orders one spouse to pay the other after separation or divorce — to cover living expenses. The amount depends on income, lifestyle and needs, and courts can grant interim (temporary) maintenance quickly.",
      meaningKn:"ಬೇರ್ಪಡೆ ಅಥವಾ ವಿಚ್ಛೇದನದ ನಂತರ ಜೀವನ ವೆಚ್ಚಕ್ಕಾಗಿ ಒಂದು ಸಂಗಾತಿ ಇನ್ನೊಬ್ಬರಿಗೆ ಪಾವತಿಸಬೇಕೆಂದು ನ್ಯಾಯಾಲಯ ಆದೇಶಿಸುವ ಆರ್ಥಿಕ ನೆರವೇ ಜೀವನಾಂಶ.",
      steps:["File a maintenance petition in the family court","Court assesses both sides' income and expenses","Interim maintenance can be ordered within weeks","Final order fixes the monthly amount","Non-payment can be enforced through the court"],
      timeEn:"Interim: 1 – 3 months · Final: 6 – 18 months", timeKn:"ಮಧ್ಯಂತರ: 1 – 3 ತಿಂಗಳು · ಅಂತಿಮ: 6 – 18 ತಿಂಗಳು",
      costEn:"Lawyer fees ₹10,000 – ₹50,000 · Amount depends on income", costKn:"ವಕೀಲರ ಶುಲ್ಕ ₹10,000 – ₹50,000 · ಮೊತ್ತ ಆದಾಯವನ್ನು ಅವಲಂಬಿಸಿರುತ್ತದೆ"
    },
    {
      id:"domestic-violence", category:"family",
      en:"Domestic Violence Protection", kn:"ಕೌಟುಂಬಿಕ ಹಿಂಸೆ ರಕ್ಷಣೆ",
      keywords:["domestic violence","dv act","protection order","abuse","harassment wife"],
      meaningEn:"The Protection of Women from Domestic Violence Act, 2005 protects women from physical, verbal, emotional, sexual or economic abuse at home. You can get a protection order, residence rights and monetary relief — and free help is available through Protection Officers and NALSA legal aid.",
      meaningKn:"ಕೌಟುಂಬಿಕ ಹಿಂಸೆಯಿಂದ ಮಹಿಳೆಯರ ರಕ್ಷಣಾ ಕಾಯ್ದೆ, 2005 ಮನೆಯಲ್ಲಿ ದೈಹಿಕ, ಮೌಖಿಕ, ಭಾವನಾತ್ಮಕ, ಲೈಂಗಿಕ ಅಥವಾ ಆರ್ಥಿಕ ದೌರ್ಜನ್ಯದಿಂದ ಮಹಿಳೆಯರನ್ನು ರಕ್ಷಿಸುತ್ತದೆ.",
      steps:["Complain to the police, a Protection Officer, or directly to the magistrate","Ask for an interim protection order — granted within days","Attend the hearing with your evidence","Court can order residence rights, maintenance and compensation","Violation of the order is punishable"],
      timeEn:"Protection order: within days · Full case: 6 – 12 months", timeKn:"ರಕ್ಷಣಾ ಆದೇಶ: ಕೆಲವು ದಿನಗಳಲ್ಲಿ · ಪೂರ್ಣ ಪ್ರಕರಣ: 6 – 12 ತಿಂಗಳು",
      costEn:"Free via Protection Officer · NALSA legal aid available", costKn:"ರಕ್ಷಣಾ ಅಧಿಕಾರಿ ಮೂಲಕ ಉಚಿತ · NALSA ಕಾನೂನು ನೆರವು ಲಭ್ಯ"
    },
    {
      id:"child-custody", category:"family",
      en:"Child Custody", kn:"ಮಕ್ಕಳ ಪಾಲನೆ",
      keywords:["custody","child custody","visitation","guardian","child"],
      meaningEn:"When parents separate, the court decides who the child lives with (custody) and how the other parent stays in touch (visitation). The single most important factor is the child's welfare — not automatically the father or the mother.",
      meaningKn:"ಪೋಷಕರು ಬೇರ್ಪಟ್ಟಾಗ ಮಗು ಯಾರೊಂದಿಗೆ ವಾಸಿಸಬೇಕು (ಪಾಲನೆ) ಮತ್ತು ಇನ್ನೊಬ್ಬ ಪೋಷಕರು ಹೇಗೆ ಸಂಪರ್ಕದಲ್ಲಿರಬೇಕು (ಭೇಟಿ ಹಕ್ಕು) ಎಂದು ನ್ಯಾಯಾಲಯ ನಿರ್ಧರಿಸುತ್ತದೆ.",
      steps:["File a custody petition in the family court","Attend mediation to try an amicable arrangement","Court considers the child's age, welfare and wishes","Interim custody / visitation is fixed early","Final custody order is passed"],
      timeEn:"Usually 6 months – 2 years", timeKn:"ಸಾಮಾನ್ಯವಾಗಿ 6 ತಿಂಗಳು – 2 ವರ್ಷಗಳು",
      costEn:"Lawyer fees ₹20,000 – ₹1,00,000+", costKn:"ವಕೀಲರ ಶುಲ್ಕ ₹20,000 – ₹1,00,000+"
    },
    {
      id:"property-dispute", category:"property",
      en:"Property / Land Dispute", kn:"ಆಸ್ತಿ / ಭೂ ವಿವಾದ",
      keywords:["property","land dispute","partition","title","ownership","boundary"],
      meaningEn:"Property disputes arise over ownership, boundaries, possession or inheritance of land and houses. The golden rule: the person with clear, registered title documents usually wins. Always verify title, check for loans/mortgages, and get an encumbrance certificate before buying.",
      meaningKn:"ಭೂಮಿ ಮತ್ತು ಮನೆಗಳ ಮಾಲೀಕತ್ವ, ಗಡಿ, ಸ್ವಾಧೀನ ಅಥವಾ ಉತ್ತರಾಧಿಕಾರದ ಬಗ್ಗೆ ಆಸ್ತಿ ವಿವಾದಗಳು ಉದ್ಭವಿಸುತ್ತವೆ. ಸುವರ್ಣ ನಿಯಮ: ಸ್ಪಷ್ಟ, ನೋಂದಾಯಿತ ಮಾಲೀಕತ್ವ ದಾಖಲೆಗಳಿರುವ ವ್ಯಕ್ತಿ ಸಾಮಾನ್ಯವಾಗಿ ಗೆಲ್ಲುತ್ತಾರೆ.",
      steps:["Collect and verify all title documents (sale deed, khata, EC)","Send a legal notice to the other party","File a civil suit (declaration / partition / injunction)","Both sides present documents, witnesses and arguments","Court passes a decree; get it executed if needed"],
      timeEn:"Typically 2 – 10 years in civil court", timeKn:"ಸಿವಿಲ್ ನ್ಯಾಯಾಲಯದಲ್ಲಿ ಸಾಮಾನ್ಯವಾಗಿ 2 – 10 ವರ್ಷಗಳು",
      costEn:"Court fee ~1–7% of property value + lawyer fees", costKn:"ಆಸ್ತಿ ಮೌಲ್ಯದ ~1–7% ನ್ಯಾಯಾಲಯ ಶುಲ್ಕ + ವಕೀಲರ ಶುಲ್ಕ"
    },
    {
      id:"tenant-eviction", category:"property",
      en:"Tenant Eviction", kn:"ಬಾಡಿಗೆದಾರರ ತೆರವು",
      keywords:["eviction","tenant","rent","landlord","tenant removal","rent control"],
      meaningEn:"A landlord cannot simply throw a tenant out or cut water/power — eviction must go through the court (or Rent Authority under state Rent Acts). Valid grounds include unpaid rent, misuse of property, or the owner's genuine personal need.",
      meaningKn:"ಮನೆಮಾಲೀಕರು ಬಾಡಿಗೆದಾರರನ್ನು ಸುಮ್ಮನೆ ಹೊರಹಾಕುವಂತಿಲ್ಲ ಅಥವಾ ನೀರು/ವಿದ್ಯುತ್ ಕಡಿತಗೊಳಿಸುವಂತಿಲ್ಲ — ತೆರವು ನ್ಯಾಯಾಲಯದ (ಅಥವಾ ರಾಜ್ಯ ಬಾಡಿಗೆ ಕಾಯ್ದೆಯಡಿ ಬಾಡಿಗೆ ಪ್ರಾಧಿಕಾರ) ಮೂಲಕವೇ ಆಗಬೇಕು.",
      steps:["Send a legal notice asking the tenant to vacate","File an eviction petition before the court / Rent Authority","Attend hearings and prove valid grounds","Obtain the eviction order","Get it executed through the court if the tenant doesn't leave"],
      timeEn:"Usually 6 months – 2 years", timeKn:"ಸಾಮಾನ್ಯವಾಗಿ 6 ತಿಂಗಳು – 2 ವರ್ಷಗಳು",
      costEn:"Lawyer fees ₹15,000 – ₹75,000+", costKn:"ವಕೀಲರ ಶುಲ್ಕ ₹15,000 – ₹75,000+"
    },
    {
      id:"property-registration", category:"property",
      en:"Property Registration", kn:"ಆಸ್ತಿ ನೋಂದಣಿ",
      keywords:["registration","sale deed","registry","stamp duty","sub registrar"],
      meaningEn:"Registering your property deal at the sub-registrar's office is what makes you the legal owner in government records. You pay stamp duty + registration fee, both parties sign before the registrar, and you receive the registered sale deed.",
      meaningKn:"ಉಪ-ನೋಂದಣಾಧಿಕಾರಿ ಕಚೇರಿಯಲ್ಲಿ ನಿಮ್ಮ ಆಸ್ತಿ ವ್ಯವಹಾರವನ್ನು ನೋಂದಾಯಿಸುವುದೇ ಸರ್ಕಾರಿ ದಾಖಲೆಗಳಲ್ಲಿ ನಿಮ್ಮನ್ನು ಕಾನೂನುಬದ್ಧ ಮಾಲೀಕರನ್ನಾಗಿ ಮಾಡುತ್ತದೆ.",
      steps:["Draft the sale deed with all details verified","Pay stamp duty and registration fees (online in most states)","Book a slot at the sub-registrar office","Both parties sign with witnesses before the registrar","Collect the registered deed — ownership is now official"],
      timeEn:"Completed the same day at the registrar office", timeKn:"ನೋಂದಣಾಧಿಕಾರಿ ಕಚೇರಿಯಲ್ಲಿ ಅದೇ ದಿನ ಪೂರ್ಣಗೊಳ್ಳುತ್ತದೆ",
      costEn:"Stamp duty 5–7% + registration ~1% (varies by state)", costKn:"ಸ್ಟಾಂಪ್ ಡ್ಯೂಟಿ 5–7% + ನೋಂದಣಿ ~1% (ರಾಜ್ಯವನ್ನು ಅವಲಂಬಿಸಿ)"
    },
    {
      id:"cyber-crime", category:"cyber",
      en:"Cyber Crime Complaint", kn:"ಸೈಬರ್ ಅಪರಾಧ ದೂರು",
      keywords:["cyber","online fraud","phishing","otp fraud","hacking","upi fraud","scam","1930"],
      meaningEn:"Fell for a fake OTP call, UPI fraud or online scam? Call the national helpline 1930 immediately and file a complaint at cybercrime.gov.in. Reporting within the 'golden hours' greatly improves the chance of freezing the fraudster's account and recovering your money.",
      meaningKn:"ನಕಲಿ OTP ಕರೆ, UPI ವಂಚನೆ ಅಥವಾ ಆನ್‌ಲೈನ್ ಮೋಸಕ್ಕೆ ಬಲಿಯಾದಿರಾ? ತಕ್ಷಣ ರಾಷ್ಟ್ರೀಯ ಸಹಾಯವಾಣಿ 1930 ಗೆ ಕರೆ ಮಾಡಿ ಮತ್ತು cybercrime.gov.in ನಲ್ಲಿ ದೂರು ಸಲ್ಲಿಸಿ.",
      steps:["Call 1930 (national cyber helpline) immediately","File a complaint at cybercrime.gov.in with screenshots & transaction IDs","Visit your local cyber cell with ID proof and evidence","An FIR is registered and investigation begins","Track your complaint with the acknowledgement number"],
      timeEn:"Report within hours for the best recovery chance", timeKn:"ಉತ್ತಮ ಮರುಪಡೆಯುವಿಕೆಗಾಗಿ ಕೆಲವು ಗಂಟೆಗಳೊಳಗೆ ವರದಿ ಮಾಡಿ",
      costEn:"Completely free to report", costKn:"ವರದಿ ಮಾಡಲು ಸಂಪೂರ್ಣ ಉಚಿತ"
    },
    {
      id:"consumer-complaint", category:"consumer",
      en:"Consumer Complaint", kn:"ಗ್ರಾಹಕ ದೂರು",
      keywords:["consumer","complaint","refund","defective","e-daakhil","cheated","product"],
      meaningEn:"Cheated by a defective product, poor service or undelivered order? Under the Consumer Protection Act 2019 you can file a complaint in the Consumer Commission — even online via the e-Daakhil portal — and claim refund, replacement or compensation.",
      meaningKn:"ದೋಷಪೂರಿತ ಉತ್ಪನ್ನ, ಕಳಪೆ ಸೇವೆ ಅಥವಾ ತಲುಪದ ಆರ್ಡರ್‌ನಿಂದ ಮೋಸ ಹೋದಿರಾ? ಗ್ರಾಹಕ ರಕ್ಷಣಾ ಕಾಯ್ದೆ 2019 ರ ಅಡಿಯಲ್ಲಿ ಗ್ರಾಹಕ ಆಯೋಗದಲ್ಲಿ ದೂರು ಸಲ್ಲಿಸಬಹುದು — ಇ-ದಾಖಿಲ್ ಪೋರ್ಟಲ್ ಮೂಲಕ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿಯೂ.",
      steps:["Send a written notice to the seller asking for refund / fix","File your complaint at edaakhil.nic.in with bills and photos","Attend the hearing (often via video call)","The commission orders refund, replacement or compensation"],
      timeEn:"Typically 3 – 12 months", timeKn:"ಸಾಮಾನ್ಯವಾಗಿ 3 – 12 ತಿಂಗಳು",
      costEn:"Nominal fee ₹100 – ₹5,000 based on claim value", costKn:"ಹಕ್ಕು ಮೌಲ್ಯದ ಆಧಾರದ ಮೇಲೆ ₹100 – ₹5,000 ನಾಮಮಾತ್ರ ಶುಲ್ಕ"
    }
  ];

  const NEWS_POOL = [
    { court:"Supreme Court", title:"Constitution Bench to hear electoral reforms plea next week", detail:"A 5-judge bench will examine fresh guidelines on transparent campaign funding." },
    { court:"Karnataka HC", title:"E-filing made mandatory for all civil cases", detail:"Physical filing counters to close for civil matters from next month; helpdesks at every district court." },
    { court:"Delhi HC", title:"Court directs speedy trial in 10-year-old property dispute", detail:"Bench orders day-to-day hearing, asks trial court to decide within 6 months." },
    { court:"Supreme Court", title:"SC: Free legal aid is a right, not charity", detail:"Directs all states to display NALSA helpline 15100 prominently in every police station." },
    { court:"Bombay HC", title:"WhatsApp messages admitted as evidence in tenancy row", detail:"Court holds verified chat records admissible under the Evidence Act." },
    { court:"Madras HC", title:"Lok Adalat settles 12,000 pending cases in a single day", detail:"Motor accident and bank recovery matters saw the highest settlements." },
    { court:"Supreme Court", title:"SC launches AI-assisted translation of judgments", detail:"Key judgments to be available in Hindi, Kannada, Tamil and 6 more languages." },
    { court:"Allahabad HC", title:"Court warns against misuse of arrest in civil disputes", detail:"Police directed to record reasons in writing before every arrest." }
  ];

  const LINKS = [
    { name:"eCourts Services", url:"https://ecourts.gov.in", icon:"i-landmark",
      descEn:"Check your case status, cause lists, court orders & hearing dates online.",
      descKn:"ನಿಮ್ಮ ಪ್ರಕರಣದ ಸ್ಥಿತಿ, ಕಾಸ್ ಪಟ್ಟಿ, ಆದೇಶಗಳು ಮತ್ತು ವಿಚಾರಣಾ ದಿನಾಂಕಗಳನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪರಿಶೀಲಿಸಿ." },
    { name:"Supreme Court of India", url:"https://www.sci.gov.in", icon:"i-scale",
      descEn:"Judgments, daily orders, causelists & e-filing at the apex court.",
      descKn:"ಸರ್ವೋಚ್ಚ ನ್ಯಾಯಾಲಯದ ತೀರ್ಪುಗಳು, ದೈನಂದಿನ ಆದೇಶಗಳು ಮತ್ತು ಇ-ಫೈಲಿಂಗ್." },
    { name:"India Code", url:"https://www.indiacode.nic.in", icon:"i-book",
      descEn:"Read every Indian Act and law — free, official & searchable.",
      descKn:"ಪ್ರತಿ ಭಾರತೀಯ ಕಾಯ್ದೆಯನ್ನು ಓದಿ — ಉಚಿತ, ಅಧಿಕೃತ ಮತ್ತು ಹುಡುಕಬಹುದಾದ." },
    { name:"NALSA — Free Legal Aid", url:"https://nalsa.gov.in", icon:"i-heart",
      descEn:"Free legal aid for eligible citizens · Helpline 15100.",
      descKn:"ಅರ್ಹ ನಾಗರಿಕರಿಗೆ ಉಚಿತ ಕಾನೂನು ನೆರವು · ಸಹಾಯವಾಣಿ 15100." }
  ];

  const UI = {
    navExplainer:{ en:"Explainer", kn:"ವಿವರಣೆ" },
    navCategories:{ en:"Categories", kn:"ವರ್ಗಗಳು" },
    navLive:{ en:"Live Updates", kn:"ಲೈವ್ ಅಪ್ಡೇಟ್‌ಗಳು" },
    navGoogle:{ en:"Google Search", kn:"ಗೂಗಲ್ ಹುಡುಕಾಟ" },
    navLinks:{ en:"Official Links", kn:"ಅಧಿಕೃತ ಲಿಂಕ್‌ಗಳು" },
    heroBadge:{ en:"Free legal literacy for every Indian", kn:"ಪ್ರತಿ ಭಾರತೀಯನಿಗೂ ಉಚಿತ ಕಾನೂನು ಜ್ಞಾನ" },
    heroTitleA:{ en:"My Lawyer Friend", kn:"ಮೈ ಲಾಯರ್ ಫ್ರೆಂಡ್" },
    heroTitleB:{ en:"Law Made Simple for Every Indian", kn:"ಪ್ರತಿ ಭಾರತೀಯನಿಗೂ ಸರಳ ಕಾನೂನು" },
    heroSub:{ en:"Type any legal word — bail, FIR, divorce, cheque bounce — and get a plain-language explanation: what it means, the steps, how long it takes, and what it costs. No jargon. No fear.",
             kn:"ಯಾವುದೇ ಕಾನೂನು ಪದವನ್ನು ಟೈಪ್ ಮಾಡಿ — ಜಾಮೀನು, FIR, ವಿಚ್ಛೇದನ, ಚೆಕ್ ಬೌನ್ಸ್ — ಮತ್ತು ಸರಳ ಭಾಷೆಯಲ್ಲಿ ವಿವರಣೆ ಪಡೆಯಿರಿ: ಅರ್ಥವೇನು, ಹಂತಗಳು, ಎಷ್ಟು ಸಮಯ, ಎಷ್ಟು ವೆಚ್ಚ." },
    heroPlaceholder:{ en:"Try 'bail', 'FIR', 'divorce', 'cyber fraud'…", kn:"'ಜಾಮೀನು', 'FIR', 'ವಿಚ್ಛೇದನ' ಪ್ರಯತ್ನಿಸಿ…" },
    heroExplain:{ en:"Explain", kn:"ವಿವರಿಸಿ" },
    heroPopular:{ en:"Popular right now:", kn:"ಈಗ ಜನಪ್ರಿಯ:" },
    stat1:{ en:"Legal terms explained", kn:"ವಿವರಿಸಿದ ಕಾನೂನು ಪದಗಳು" },
    stat2:{ en:"Categories covered", kn:"ವರ್ಗಗಳು" },
    stat3:{ en:"100% free forever", kn:"ಶಾಶ್ವತವಾಗಿ 100% ಉಚಿತ" },
    explKicker:{ en:"AI Legal Explainer", kn:"AI ಕಾನೂನು ವಿವರಣೆ" },
    explTitle:{ en:"Ask in plain words. Understand like a friend explained it.", kn:"ಸರಳ ಪದಗಳಲ್ಲಿ ಕೇಳಿ. ಸ್ನೇಹಿತ ವಿವರಿಸಿದಂತೆ ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ." },
    explMeaning:{ en:"What it means", kn:"ಇದರ ಅರ್ಥ" },
    explSteps:{ en:"Steps to follow", kn:"ಅನುಸರಿಸಬೇಕಾದ ಹಂತಗಳು" },
    explTime:{ en:"Time taken", kn:"ತೆಗೆದುಕೊಳ್ಳುವ ಸಮಯ" },
    explCost:{ en:"Cost involved", kn:"ಒಳಗೊಂಡ ವೆಚ್ಚ" },
    explNotFound:{ en:"We don't have a simple explainer for that yet.", kn:"ಇದಕ್ಕೆ ಸರಳ ವಿವರಣೆ ಇನ್ನೂ ನಮ್ಮಲ್ಲಿಲ್ಲ." },
    explNotFoundSub:{ en:"Try one of the popular terms below — or search it on Google for official sources.", kn:"ಕೆಳಗಿನ ಜನಪ್ರಿಯ ಪದಗಳಲ್ಲಿ ಒಂದನ್ನು ಪ್ರಯತ್ನಿಸಿ — ಅಥವಾ ಅಧಿಕೃತ ಮೂಲಗಳಿಗಾಗಿ ಗೂಗಲ್‌ನಲ್ಲಿ ಹುಡುಕಿ." },
    explGoogle:{ en:"Search with Google", kn:"ಗೂಗಲ್‌ನಲ್ಲಿ ಹುಡುಕಿ" },
    explStart:{ en:"Search a legal term above, or pick a category below to begin.", kn:"ಮೇಲೆ ಕಾನೂನು ಪದವನ್ನು ಹುಡುಕಿ, ಅಥವಾ ಪ್ರಾರಂಭಿಸಲು ಕೆಳಗೆ ವರ್ಗವನ್ನು ಆಯ್ಕೆಮಾಡಿ." },
    catKicker:{ en:"Browse by category", kn:"ವರ್ಗದ ಪ್ರಕಾರ ಬ್ರೌಸ್ ಮಾಡಿ" },
    catTitle:{ en:"Everyday legal problems, organised for you", kn:"ದೈನಂದಿನ ಕಾನೂನು ಸಮಸ್ಯೆಗಳು, ನಿಮಗಾಗಿ ವ್ಯವಸ್ಥಿತ" },
    catTerms:{ en:"explainer topics", kn:"ವಿವರಣಾ ವಿಷಯಗಳು" },
    liveKicker:{ en:"Live from the courts", kn:"ನ್ಯಾಯಾಲಯಗಳಿಂದ ಲೈವ್" },
    liveTitle:{ en:"Court updates, as they happen", kn:"ನ್ಯಾಯಾಲಯದ ಅಪ್ಡೇಟ್‌ಗಳು, ನಡೆದಂತೆ" },
    liveNote:{ en:"Demo feed — sample headlines refresh automatically", kn:"ಡೆಮೊ ಫೀಡ್ — ಮಾದರಿ ಶೀರ್ಷಿಕೆಗಳು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ರಿಫ್ರೆಶ್ ಆಗುತ್ತವೆ" },
    googKicker:{ en:"Deeper research", kn:"ಆಳವಾದ ಸಂಶೋಧನೆ" },
    googTitle:{ en:"Take it further with Google", kn:"ಗೂಗಲ್‌ನೊಂದಿಗೆ ಮುಂದುವರಿಸಿ" },
    googSub:{ en:"Need official judgments, forms or the latest news on your topic? Search Google directly — results open in a new tab.", kn:"ನಿಮ್ಮ ವಿಷಯದ ಅಧಿಕೃತ ತೀರ್ಪುಗಳು, ಫಾರ್ಮ್‌ಗಳು ಅಥವಾ ಇತ್ತೀಚಿನ ಸುದ್ದಿ ಬೇಕೇ? ನೇರವಾಗಿ ಗೂಗಲ್‌ನಲ್ಲಿ ಹುಡುಕಿ." },
    googPlaceholder:{ en:"e.g. bail application format pdf…", kn:"ಉದಾ. ಜಾಮೀನು ಅರ್ಜಿ ನಮೂನೆ…" },
    googButton:{ en:"Search Google", kn:"ಗೂಗಲ್ ಹುಡುಕಿ" },
    linksKicker:{ en:"Trusted & official", kn:"ವಿಶ್ವಾಸಾರ್ಹ ಮತ್ತು ಅಧಿಕೃತ" },
    linksTitle:{ en:"Go straight to the source", kn:"ನೇರವಾಗಿ ಮೂಲಕ್ಕೆ ಹೋಗಿ" },
    linksSub:{ en:"Skip the middlemen. These are the official Government of India portals for cases, laws and free legal aid.", kn:"ಮಧ್ಯವರ್ತಿಗಳನ್ನು ಬಿಟ್ಟುಬಿಡಿ. ಪ್ರಕರಣಗಳು, ಕಾನೂನುಗಳು ಮತ್ತು ಉಚಿತ ಕಾನೂನು ನೆರವಿಗಾಗಿ ಇವು ಭಾರತ ಸರ್ಕಾರದ ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ಗಳು." },
    linksVisit:{ en:"Visit site", kn:"ಸೈಟ್‌ಗೆ ಭೇಟಿ ನೀಡಿ" },
    footDisclaimer:{ en:"For education only — not legal advice. Laws change; always consult a qualified lawyer for your specific situation.", kn:"ಶಿಕ್ಷಣಕ್ಕಾಗಿ ಮಾತ್ರ — ಕಾನೂನು ಸಲಹೆಯಲ್ಲ. ಕಾನೂನುಗಳು ಬದಲಾಗುತ್ತವೆ; ನಿಮ್ಮ ನಿರ್ದಿಷ್ಟ ಪರಿಸ್ಥಿತಿಗಾಗಿ ಯಾವಾಗಲೂ ಅರ್ಹ ವಕೀಲರನ್ನು ಸಂಪರ್ಕಿಸಿ." },
    footTag:{ en:"Built for every common Indian · My Lawyer Friend", kn:"ಪ್ರತಿ ಸಾಮಾನ್ಯ ಭಾರತೀಯನಿಗಾಗಿ · ಮೈ ಲಾಯರ್ ಫ್ರೆಂಡ್" }
  };

  const POPULAR_TERMS = ["bail","FIR","divorce","cheque bounce","cyber fraud","consumer complaint"];

  /* =========================================================
     STATE
     ========================================================= */

  const state = {
    lang: "en",
    query: "",
    googleQuery: "",
    selectedTerm: null,
    searched: false,
    activeCategory: null,
    activeNav: "explainer",
    mobileMenuOpen: false,
    logoPulse: false,
    newsItems: [],
    newsCounter: 0,
    tickerItems: NEWS_POOL.slice(0, 6)
  };

  /* =========================================================
     HELPERS
     ========================================================= */

  const $  = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));
  const escapeHtml = (str) => String(str)
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;").replace(/'/g, "&#39;");

  const tr = (key) => UI[key] ? UI[key][state.lang] : key;

  function matchTerm(query) {
    const q = query.toLowerCase().trim();
    if (!q) return null;
    let best = null;
    for (const term of TERMS) {
      let score = 0;
      if (term.en.toLowerCase().includes(q) || q.includes(term.id.replace(/-/g, " "))) score += 6;
      for (const kw of term.keywords) {
        const k = kw.toLowerCase();
        if (k === q) score += 5;
        else if (k.includes(q) || q.includes(k)) score += 3;
      }
      if (score > 0 && (!best || score > best.score)) best = { term, score };
    }
    return best ? best.term : null;
  }

  function openGoogle(query) {
    const q = query.trim() ? `${query.trim()} legal help India` : "Indian law help";
    window.open(`https://www.google.com/search?q=${encodeURIComponent(q)}`, "_blank", "noopener,noreferrer");
  }

  function catLabel(catId) {
    const c = CATEGORIES.find(x => x.id === catId);
    return c ? (state.lang === "kn" ? c.kn : c.en) : "";
  }

  function svg(id, cls = "") {
    return `<svg class="${cls}" aria-hidden="true"><use href="#${id}"/></svg>`;
  }

  /* =========================================================
     RENDER FUNCTIONS
     ========================================================= */

  function renderTicker() {
    const items = state.tickerItems.concat(state.tickerItems);
    return `
      <div class="ticker-bar">
        <div class="ticker-inner">
          <div class="ticker-badge"><span class="dot live-dot"></span>Live</div>
          <div class="ticker-viewport">
            <div class="ticker-track">
              ${items.map(n => `<span class="ticker-item"><span class="court">${escapeHtml(n.court)}:</span> ${escapeHtml(n.title)}</span>`).join("")}
            </div>
          </div>
        </div>
      </div>`;
  }

  function renderHeader() {
    const navItems = [
      ["explainer", tr("navExplainer")],
      ["categories", tr("navCategories")],
      ["live", tr("navLive")],
      ["google", tr("navGoogle")],
      ["links", tr("navLinks")]
    ];

    const navDesktop = navItems.map(([id, label]) => `
      <button class="nav-link ${state.activeNav === id ? "is-active" : ""}"
              data-action="nav" data-target="${id}">${label}</button>
    `).join("");

    const navMobile = navItems.map(([id, label]) => `
      <button class="nav-link ${state.activeNav === id ? "is-active" : ""}"
              data-action="nav" data-target="${id}">${label}</button>
    `).join("");

    return `
      <header class="site-header">
        <div class="container header-row">
          <button class="brand ${state.logoPulse ? "is-pulsing" : ""}" data-action="home" aria-label="Go to top">
            <span class="brand-mark">${svg("i-scale")}</span>
            <span>
              <span class="brand-name gold-text">My Lawyer Friend</span>
              <span class="brand-tag">Court Case Explainer</span>
            </span>
          </button>

          <nav class="nav-desktop" aria-label="Primary">${navDesktop}</nav>

          <div class="header-actions">
            <button class="lang-btn" data-action="toggle-lang" aria-label="Toggle language">
              ${svg("i-languages")} ${state.lang === "en" ? "ಕನ್ನಡ" : "English"}
            </button>
            <button class="menu-btn" data-action="toggle-menu" aria-label="Menu" aria-expanded="${state.mobileMenuOpen}">
              ${state.mobileMenuOpen ? svg("i-close") : svg("i-menu")}
            </button>
          </div>
        </div>

        <nav class="nav-mobile ${state.mobileMenuOpen ? "is-open" : ""}" aria-label="Mobile">
          ${navMobile}
        </nav>
      </header>`;
  }

  function renderHero() {
    const chips = POPULAR_TERMS.map(q =>
      `<button class="chip" data-action="search-term" data-term="${escapeHtml(q)}">${escapeHtml(q)}</button>`
    ).join("");

    return `
      <section class="hero">
        <div class="glow glow-1"></div>
        <div class="glow glow-2 floaty"></div>
        <div class="glow glow-3 floaty"></div>

        <div class="container hero-inner">
          <div class="hero-badge anim-up">
            ${svg("i-sparkles")} ${tr("heroBadge")}
          </div>

          <h1 class="hero-title anim-up-1">
            <span class="gold-text">${tr("heroTitleA")}</span><br>
            <span style="color:#fff">${tr("heroTitleB")}</span>
          </h1>

          <p class="hero-sub anim-up-2">${tr("heroSub")}</p>

          <form class="search-shell anim-up-3" data-action="hero-search" novalidate>
            <div class="search-box glass gold-ring">
              <div class="search-field">
                ${svg("i-search")}
                <input id="hero-input" type="search" value="${escapeHtml(state.query)}"
                       placeholder="${escapeHtml(tr("heroPlaceholder"))}"
                       autocomplete="off" spellcheck="false"
                       aria-label="Search legal term">
              </div>
              <div class="search-actions">
                <button type="submit" class="btn btn-gold btn-search">${tr("heroExplain")}</button>
                <button type="button" class="btn btn-ghost" data-action="hero-google" aria-label="Search Google">
                  ${svg("i-globe")}<span class="sr-only">Google</span>
                </button>
              </div>
            </div>
          </form>

          <div class="popular-row anim-up-3">
            <span class="popular-label">${tr("heroPopular")}</span>
            ${chips}
          </div>

          <div class="stat-row anim-up-3">
            <div class="stat"><div class="stat-value gold-text">${TERMS.length}</div><div class="stat-label">${tr("stat1")}</div></div>
            <div class="stat"><div class="stat-value gold-text">${CATEGORIES.length}</div><div class="stat-label">${tr("stat2")}</div></div>
            <div class="stat"><div class="stat-value gold-text">₹0</div><div class="stat-label">${tr("stat3")}</div></div>
          </div>
        </div>

        <div class="hero-divider"></div>
      </section>`;
  }

  function renderExplainer() {
    const term = state.selectedTerm;

    if (term) {
      const name = state.lang === "kn" ? term.kn : term.en;
      const meaning = state.lang === "kn" ? term.meaningKn : term.meaningEn;
      const timeVal = state.lang === "kn" ? term.timeKn : term.timeEn;
      const costVal = state.lang === "kn" ? term.costKn : term.costEn;

      const stepsHtml = term.steps.map((s, i) => `
        <li class="step">
          <span class="step-num">${i + 1}</span>
          <span class="step-text">${escapeHtml(s)}</span>
        </li>`).join("");

      return `
        <div class="explainer-wrap">
          <div class="term-panel panel-in">
            <div class="panel-head">
              <div class="panel-kicker">${svg("i-sparkles")} ${catLabel(term.category)}</div>
              <h3 class="panel-title">${escapeHtml(name)}</h3>
            </div>
            <div class="panel-body">
              <div class="panel-section">
                <div class="panel-label">${svg("i-book")} ${tr("explMeaning")}</div>
                <p class="panel-text">${escapeHtml(meaning)}</p>
              </div>

              <div class="panel-section">
                <div class="panel-label">${svg("i-list")} ${tr("explSteps")}</div>
                <ol class="step-list">${stepsHtml}</ol>
              </div>

              <div class="info-grid">
                <div class="info-box">
                  <div class="panel-label">${svg("i-clock")} ${tr("explTime")}</div>
                  <div class="value">${escapeHtml(timeVal)}</div>
                </div>
                <div class="info-box">
                  <div class="panel-label">${svg("i-rupee")} ${tr("explCost")}</div>
                  <div class="value">${escapeHtml(costVal)}</div>
                </div>
              </div>

              <button class="btn btn-ghost" data-action="google-term" data-term="${escapeHtml(term.en)}">
                ${svg("i-globe")} ${tr("explGoogle")} ${svg("i-chevron-right")}
              </button>
            </div>
          </div>
        </div>`;
    }

    if (state.searched) {
      const chips = POPULAR_TERMS.map(q =>
        `<button class="chip" data-action="search-term" data-term="${escapeHtml(q)}">${escapeHtml(q)}</button>`
      ).join("");
      return `
        <div class="notfound anim-up">
          <div class="alert-icon">${svg("i-alert")}</div>
          <h3>${tr("explNotFound")}</h3>
          <p>${tr("explNotFoundSub")}</p>
          <div class="chip-row">${chips}</div>
          <button class="btn btn-gold" data-action="google-query" data-query="${escapeHtml(state.query)}">
            ${svg("i-globe")} ${tr("explGoogle")}
          </button>
        </div>`;
    }

    return `
      <div class="explainer-empty">
        ${svg("i-scale")}
        <p>${tr("explStart")}</p>
      </div>`;
  }

  function renderCategories() {
    const cards = CATEGORIES.map(c => {
      const isActive = state.activeCategory === c.id;
      const count = TERMS.filter(t => t.category === c.id).length;
      return `
        <button class="category-card ${isActive ? "is-active" : ""}"
                data-action="select-category" data-id="${c.id}"
                aria-pressed="${isActive}">
          <span class="cat-icon">${svg(c.icon)}</span>
          <div class="cat-title">${state.lang === "kn" ? c.kn : c.en}</div>
          <div class="cat-sub">${state.lang === "kn" ? c.tagKn : c.tagEn}</div>
          <div class="cat-count">${count} ${tr("catTerms")}</div>
        </button>`;
    }).join("");

    let filtered = "";
    if (state.activeCategory) {
      const list = TERMS.filter(t => t.category === state.activeCategory);
      filtered = `
        <div class="term-grid anim-up">
          ${list.map(t => {
            const name = state.lang === "kn" ? t.kn : t.en;
            const meaning = state.lang === "kn" ? t.meaningKn : t.meaningEn;
            return `
              <button class="term-card" data-action="explain-term" data-id="${t.id}">
                <h3>${escapeHtml(name)}</h3>
                <p>${escapeHtml(meaning)}</p>
                <span class="term-cta">${tr("heroExplain")} ${svg("i-arrow-right")}</span>
              </button>`;
          }).join("")}
        </div>`;
    }

    return `
      <section id="categories" class="section section-tinted">
        <div class="container">
          <div class="section-head">
            <div class="kicker">${tr("catKicker")}</div>
            <h2 class="section-title">${tr("catTitle")}</h2>
          </div>
          <div class="category-grid">${cards}</div>
          ${filtered}
        </div>
      </section>`;
  }

  function renderLive() {
    const cards = state.newsItems.map((n, i) => `
      <article class="news-card">
        ${i === 0 ? `<span class="news-live"><span class="dot live-dot"></span>Live</span>` : ""}
        <div class="news-court">${svg("i-zap")} ${escapeHtml(n.court)}</div>
        <h3 class="news-title">${escapeHtml(n.title)}</h3>
        <p class="news-detail">${escapeHtml(n.detail)}</p>
        <div class="news-time">${svg("i-clock")} ${escapeHtml(n.stamp)}</div>
      </article>
    `).join("");

    return `
      <section id="live" class="section">
        <div class="container">
          <div class="section-head" style="text-align:left; display:flex; flex-direction:column; gap:.75rem;">
            <div style="display:flex; flex-direction:column; gap:.5rem;">
              <div class="kicker"><span class="live-dot" style="width:.6rem;height:.6rem;border-radius:9999px;background:var(--red-500);display:inline-block"></span> ${tr("liveKicker")}</div>
              <h2 class="section-title">${tr("liveTitle")}</h2>
            </div>
            <p style="font-size:.75rem;color:var(--ink-500);font-style:italic;">${tr("liveNote")}</p>
          </div>
          <div class="news-grid">${cards}</div>
        </div>
      </section>`;
  }

  function renderGoogle() {
    return `
      <section id="google" class="section section-tinted google-wrap">
        <div class="google-glow"></div>
        <div class="container google-inner">
          <div class="kicker">${tr("googKicker")}</div>
          <h2 class="section-title" style="margin-bottom:.75rem;">${tr("googTitle")}</h2>
          <p class="google-sub">${tr("googSub")}</p>

          <form class="google-form glass gold-ring" data-action="google-search" novalidate>
            <div class="google-field">
              <span class="g-mark">G</span>
              <input id="google-input" type="search" value="${escapeHtml(state.googleQuery)}"
                     placeholder="${escapeHtml(tr("googPlaceholder"))}"
                     autocomplete="off" spellcheck="false"
                     aria-label="Google search">
            </div>
            <button type="submit" class="btn btn-gold" style="padding-inline:1.75rem; border-radius:.75rem;">
              ${svg("i-search")} ${tr("googButton")}
            </button>
          </form>

          <p class="google-note">Opens google.com in a new tab · Free forever</p>
        </div>
      </section>`;
  }

  function renderLinks() {
    const cards = LINKS.map(l => `
      <a class="link-card" href="${escapeHtml(l.url)}" target="_blank" rel="noopener noreferrer">
        <span class="link-icon">${svg(l.icon)}</span>
        <div class="link-name">${escapeHtml(l.name)}</div>
        <p class="link-desc">${state.lang === "kn" ? l.descKn : l.descEn}</p>
        <span class="link-cta">${tr("linksVisit")} ${svg("i-external")}</span>
      </a>
    `).join("");

    return `
      <section id="links" class="section">
        <div class="container">
          <div class="section-head">
            <div class="kicker">${tr("linksKicker")}</div>
            <h2 class="section-title" style="margin-bottom:1rem;">${tr("linksTitle")}</h2>
            <p style="color:var(--ink-400); font-size:.9rem; max-width:42rem; margin:0 auto; line-height:1.7;">${tr("linksSub")}</p>
          </div>
          <div class="links-grid">${cards}</div>
        </div>
      </section>`;
  }

  function renderFooter() {
    return `
      <footer class="site-footer">
        <div class="container section">
          <div class="footer-top">
            <div class="footer-brand">
              <span class="brand-mark">${svg("i-scale")}</span>
              <div>
                <div class="font-display gold-text" style="font-weight:700;font-size:1.0625rem;">My Lawyer Friend</div>
                <div style="font-size:.5625rem;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-500);margin-top:.2rem;">Your Friend in Law · Bridge to Justice</div>
              </div>
            </div>
            <div class="footer-tagline">${svg("i-badge")} ${tr("footTag")}</div>
          </div>

          <div class="disclaimer">
            ${svg("i-alert")}
            <p><strong>Disclaimer: </strong>${tr("footDisclaimer")}</p>
          </div>

          <div class="copyright">© ${new Date().getFullYear()} My Lawyer Friend · A student portfolio project for legal literacy</div>
        </div>
      </footer>`;
  }

  function renderExplainerSection() {
    return `
      <section id="explainer" class="section">
        <div class="container">
          <div class="section-head">
            <div class="kicker">${svg("i-gavel")} ${tr("explKicker")}</div>
            <h2 class="section-title">${tr("explTitle")}</h2>
          </div>
          ${renderExplainer()}
        </div>
      </section>`;
  }

  function render() {
    $("#app").innerHTML = `
      ${renderTicker()}
      ${renderHeader()}
      ${renderHero()}
      ${renderExplainerSection()}
      ${renderCategories()}
      ${renderLive()}
      ${renderGoogle()}
      ${renderLinks()}
      ${renderFooter()}
    `;
  }

  /* =========================================================
     ACTIONS
     ========================================================= */

  function setQuery(q) {
    state.query = q;
    const input = $("#hero-input");
    if (input && input.value !== q) input.value = q;
  }

  function runExplain(q) {
    const term = matchTerm(q);
    state.selectedTerm = term;
    state.searched = true;
    state.activeCategory = null;
    state.query = q;
    render();
    document.getElementById("explainer")?.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  function navigateTo(section) {
    state.activeNav = section;
    state.mobileMenuOpen = false;
    if (section === "top") {
      window.scrollTo({ top: 0, behavior: "smooth" });
    } else {
      document.getElementById(section)?.scrollIntoView({ behavior: "smooth", block: "start" });
    }
    render();
  }

  function toggleLang() {
    state.lang = state.lang === "en" ? "kn" : "en";
    render();
  }

  function toggleMenu() {
    state.mobileMenuOpen = !state.mobileMenuOpen;
    render();
  }

  function pulseLogo() {
    state.logoPulse = true;
    render();
    setTimeout(() => { state.logoPulse = false; render(); }, 700);
  }

  function selectCategory(id) {
    state.activeCategory = state.activeCategory === id ? null : id;
    render();
  }

  function explainTerm(id) {
    const t = TERMS.find(x => x.id === id);
    if (!t) return;
    state.selectedTerm = t;
    state.searched = true;
    setQuery(t.en);
    render();
    document.getElementById("explainer")?.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  /* =========================================================
     EVENT DELEGATION
     ========================================================= */

  document.addEventListener("click", (e) => {
    const el = e.target.closest("[data-action]");
    if (!el) return;
    const action = el.dataset.action;

    switch (action) {
      case "home":
        navigateTo("top");
        pulseLogo();
        break;
      case "nav":
        navigateTo(el.dataset.target);
        break;
      case "toggle-lang":
        toggleLang();
        break;
      case "toggle-menu":
        toggleMenu();
        break;
      case "select-category":
        selectCategory(el.dataset.id);
        break;
      case "explain-term":
        explainTerm(el.dataset.id);
        break;
      case "search-term":
        setQuery(el.dataset.term);
        runExplain(el.dataset.term);
        break;
      case "hero-google": {
        const input = $("#hero-input");
        openGoogle(input ? input.value : state.query);
        break;
      }
      case "google-term":
        openGoogle(el.dataset.term);
        break;
      case "google-query":
        openGoogle(el.dataset.query || state.query);
        break;
    }
  });

  document.addEventListener("input", (e) => {
    if (e.target.id === "hero-input") state.query = e.target.value;
    if (e.target.id === "google-input") state.googleQuery = e.target.value;
  });

  document.addEventListener("submit", (e) => {
    const form = e.target.closest("form[data-action]");
    if (!form) return;
    e.preventDefault();
    const action = form.dataset.action;

    if (action === "hero-search") {
      const input = $("#hero-input");
      runExplain(input ? input.value : state.query);
    } else if (action === "google-search") {
      const input = $("#google-input");
      openGoogle(input ? input.value : state.googleQuery);
    }
  });

  // Esc closes mobile menu
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && state.mobileMenuOpen) {
      state.mobileMenuOpen = false;
      render();
    }
  });

  /* =========================================================
     NEWS FEED TICKER (live demo)
     ========================================================= */

  function initNews() {
    state.newsItems = NEWS_POOL.slice(0, 4).map((n, i) => ({
      ...n,
      stamp: i === 0 ? "Just now" : `${(i + 1) * 7} min ago`
    }));
    state.newsCounter = 4;
  }

  function rotateNews() {
    const next = NEWS_POOL[state.newsCounter % NEWS_POOL.length];
    state.newsCounter += 1;
    state.newsItems = [
      { ...next, stamp: "Just now" },
      ...state.newsItems.slice(0, 3)
    ];
    render();
  }

  /* =========================================================
     BOOT
     ========================================================= */

  initNews();
  render();
  setInterval(rotateNews, 9000);

})();
</script>

</body>
</html>
