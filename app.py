<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>My Lawyer Friend · Law Made Simple</title>
  <style>
    /* ===== Fonts & base ===== */
    @import url("https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap");

    :root {
      --gold: #d4af37;
      --gold-light: #f6e27a;
      --gold-deep: #c9962e;
      --navy-900: #070d1f;
      --navy-800: #0a1128;
      --navy-700: #0d1730;
      --navy-600: #131f42;
      --slate-100: #eef1f8;
      --slate-200: #e2e8f0;
      --slate-300: #cbd5e1;
      --slate-400: #94a3b8;
      --slate-500: #64748b;
      --amber-300: #fcd34d;
      --amber-400: #fbbf24;
      --amber-500: #f59e0b;
      --amber-600: #d97706;
    }

    *,
    *::before,
    *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      scroll-padding-top: 84px;
    }

    body {
      background-color: var(--navy-900);
      color: var(--slate-100);
      font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      overflow-x: clip;
    }

    /* ===== Utility ===== */
    .container {
      max-width: 80rem;
      margin: 0 auto;
      padding: 0 1.25rem;
    }

    @media (min-width: 640px) {
      .container {
        padding: 0 1.5rem;
      }
    }

    /* ===== Colors & gradients ===== */
    .text-gold-gradient {
      background: linear-gradient(120deg, #f6e27a 0%, #d4af37 35%, #f9eec3 55%, #c9962e 80%, #f6e27a 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
    }

    .font-display {
      font-family: 'Fraunces', Georgia, 'Times New Roman', serif;
    }

    /* ===== Glass ===== */
    .glass {
      background: linear-gradient(145deg, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0.025));
      border: 1px solid rgba(212, 175, 55, 0.16);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
    }

    .glass-strong {
      background: linear-gradient(145deg, rgba(20, 30, 60, 0.85), rgba(10, 16, 36, 0.92));
      border: 1px solid rgba(212, 175, 55, 0.22);
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
    }

    .gold-ring:focus-within {
      border-color: rgba(212, 175, 55, 0.65);
      box-shadow: 0 0 0 4px rgba(212, 175, 55, 0.15), 0 18px 50px -18px rgba(212, 175, 55, 0.35);
    }

    /* ===== Animations ===== */
    @keyframes fadeUp {
      0% { opacity: 0; transform: translateY(22px); }
      100% { opacity: 1; transform: translateY(0); }
    }

    .animate-fade-up {
      animation: fadeUp 0.7s cubic-bezier(0.22, 1, 0.36, 1) both;
    }
    .animate-fade-up-1 { animation: fadeUp 0.7s cubic-bezier(0.22, 1, 0.36, 1) 0.08s both; }
    .animate-fade-up-2 { animation: fadeUp 0.7s cubic-bezier(0.22, 1, 0.36, 1) 0.16s both; }
    .animate-fade-up-3 { animation: fadeUp 0.7s cubic-bezier(0.22, 1, 0.36, 1) 0.24s both; }

    @keyframes pulseDot {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.6); opacity: 0.55; }
    }

    .live-dot {
      animation: pulseDot 1.6s ease-in-out infinite;
    }

    @keyframes ticker {
      0% { transform: translateX(0); }
      100% { transform: translateX(-50%); }
    }

    .ticker-track {
      animation: ticker 40s linear infinite;
    }
    .ticker-track:hover {
      animation-play-state: paused;
    }

    @keyframes floaty {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-18px); }
    }

    .animate-floaty {
      animation: floaty 9s ease-in-out infinite;
    }

    /* ===== Grid bg ===== */
    .bg-grid-gold {
      background-image:
        linear-gradient(rgba(212, 175, 55, 0.055) 1px, transparent 1px),
        linear-gradient(90deg, rgba(212, 175, 55, 0.055) 1px, transparent 1px);
      background-size: 44px 44px;
      mask-image: radial-gradient(ellipse 90% 70% at 50% 30%, #000 30%, transparent 75%);
      -webkit-mask-image: radial-gradient(ellipse 90% 70% at 50% 30%, #000 30%, transparent 75%);
    }

    /* ===== Scrollbar ===== */
    ::-webkit-scrollbar { width: 10px; }
    ::-webkit-scrollbar-track { background: var(--navy-900); }
    ::-webkit-scrollbar-thumb {
      background: #2a3358;
      border-radius: 8px;
      border: 2px solid var(--navy-900);
    }
    ::-webkit-scrollbar-thumb:hover { background: var(--gold); }

    ::selection {
      background: rgba(212, 175, 55, 0.35);
      color: #fff;
    }

    /* ===== Layout helpers ===== */
    .flex { display: flex; }
    .flex-col { flex-direction: column; }
    .flex-wrap { flex-wrap: wrap; }
    .items-center { align-items: center; }
    .items-start { align-items: flex-start; }
    .justify-center { justify-content: center; }
    .justify-between { justify-content: space-between; }
    .gap-1 { gap: 0.25rem; }
    .gap-1\.5 { gap: 0.375rem; }
    .gap-2 { gap: 0.5rem; }
    .gap-3 { gap: 0.75rem; }
    .gap-3\.5 { gap: 0.875rem; }
    .gap-4 { gap: 1rem; }
    .gap-6 { gap: 1.5rem; }
    .gap-7 { gap: 1.75rem; }

    .grid { display: grid; }
    .grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }

    @media (min-width: 640px) {
      .sm\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
      .sm\:flex-row { flex-direction: row; }
      .sm\:items-end { align-items: flex-end; }
      .sm\:justify-between { justify-content: space-between; }
    }

    @media (min-width: 1024px) {
      .lg\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
      .lg\:grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
      .lg\:flex { display: flex; }
      .lg\:hidden { display: none; }
    }

    /* ===== Spacing ===== */
    .p-2 { padding: 0.5rem; }
    .p-4 { padding: 1rem; }
    .p-5 { padding: 1.25rem; }
    .p-6 { padding: 1.5rem; }
    .p-8 { padding: 2rem; }
    .px-2 { padding-left: 0.5rem; padding-right: 0.5rem; }
    .px-2\.5 { padding-left: 0.625rem; padding-right: 0.625rem; }
    .px-3 { padding-left: 0.75rem; padding-right: 0.75rem; }
    .px-3\.5 { padding-left: 0.875rem; padding-right: 0.875rem; }
    .px-4 { padding-left: 1rem; padding-right: 1rem; }
    .px-5 { padding-left: 1.25rem; padding-right: 1.25rem; }
    .px-6 { padding-left: 1.5rem; padding-right: 1.5rem; }
    .px-7 { padding-left: 1.75rem; padding-right: 1.75rem; }
    .py-1 { padding-top: 0.25rem; padding-bottom: 0.25rem; }
    .py-1\.5 { padding-top: 0.375rem; padding-bottom: 0.375rem; }
    .py-2 { padding-top: 0.5rem; padding-bottom: 0.5rem; }
    .py-2\.5 { padding-top: 0.625rem; padding-bottom: 0.625rem; }
    .py-3 { padding-top: 0.75rem; padding-bottom: 0.75rem; }
    .py-4 { padding-top: 1rem; padding-bottom: 1rem; }
    .py-6 { padding-top: 1.5rem; padding-bottom: 1.5rem; }
    .py-10 { padding-top: 2.5rem; padding-bottom: 2.5rem; }
    .py-14 { padding-top: 3.5rem; padding-bottom: 3.5rem; }

    .mb-1\.5 { margin-bottom: 0.375rem; }
    .mb-2 { margin-bottom: 0.5rem; }
    .mb-2\.5 { margin-bottom: 0.625rem; }
    .mb-3 { margin-bottom: 0.75rem; }
    .mb-4 { margin-bottom: 1rem; }
    .mb-5 { margin-bottom: 1.25rem; }
    .mb-6 { margin-bottom: 1.5rem; }
    .mb-7 { margin-bottom: 1.75rem; }
    .mb-8 { margin-bottom: 2rem; }
    .mb-10 { margin-bottom: 2.5rem; }
    .mt-0\.5 { margin-top: 0.125rem; }
    .mt-1 { margin-top: 0.25rem; }
    .mt-2 { margin-top: 0.5rem; }
    .mt-3 { margin-top: 0.75rem; }
    .mt-4 { margin-top: 1rem; }
    .mt-5 { margin-top: 1.25rem; }
    .mt-8 { margin-top: 2rem; }
    .mt-10 { margin-top: 2.5rem; }
    .-ml-2 { margin-left: -0.5rem; }

    /* ===== Typography ===== */
    .text-xs { font-size: 0.75rem; line-height: 1rem; }
    .text-sm { font-size: 0.875rem; line-height: 1.25rem; }
    .text-base { font-size: 1rem; line-height: 1.5rem; }
    .text-lg { font-size: 1.125rem; line-height: 1.75rem; }
    .text-xl { font-size: 1.25rem; line-height: 1.75rem; }
    .text-2xl { font-size: 1.5rem; line-height: 2rem; }
    .text-3xl { font-size: 1.875rem; line-height: 2.25rem; }
    .text-4xl { font-size: 2.25rem; line-height: 2.5rem; }

    @media (min-width: 640px) {
      .sm\:text-3xl { font-size: 1.875rem; line-height: 2.25rem; }
      .sm\:text-4xl { font-size: 2.25rem; line-height: 2.5rem; }
      .sm\:text-5xl { font-size: 3rem; line-height: 1; }
      .sm\:text-6xl { font-size: 3.75rem; line-height: 1; }
      .sm\:text-lg { font-size: 1.125rem; line-height: 1.75rem; }
      .sm\:text-xl { font-size: 1.25rem; line-height: 1.75rem; }
      .sm\:text-base { font-size: 1rem; line-height: 1.5rem; }
    }

    @media (min-width: 1024px) {
      .lg\:text-7xl { font-size: 4.5rem; line-height: 1; }
    }

    .font-bold { font-weight: 700; }
    .font-semibold { font-weight: 600; }
    .font-medium { font-weight: 500; }
    .uppercase { text-transform: uppercase; }
    .tracking-wider { letter-spacing: 0.05em; }
    .tracking-tight { letter-spacing: -0.025em; }
    .leading-none { line-height: 1; }
    .leading-tight { line-height: 1.25; }
    .leading-snug { line-height: 1.375; }
    .leading-relaxed { line-height: 1.625; }
    .leading-\[1\.05\] { line-height: 1.05; }

    .text-center { text-align: center; }
    .text-left { text-align: left; }

    /* ===== Colors ===== */
    .text-white { color: #fff; }
    .text-slate-100 { color: var(--slate-100); }
    .text-slate-200 { color: var(--slate-200); }
    .text-slate-300 { color: var(--slate-300); }
    .text-slate-400 { color: var(--slate-400); }
    .text-slate-500 { color: var(--slate-500); }
    .text-slate-600 { color: #475569; }
    .text-amber-200 { color: #fde68a; }
    .text-amber-300 { color: var(--amber-300); }
    .text-red-400 { color: #f87171; }
    .text-\[\#0a1128\] { color: var(--navy-800); }

    .bg-\[\#070d1f\] { background-color: var(--navy-900); }
    .bg-\[\#0a1128\] { background-color: var(--navy-800); }
    .bg-\[\#0a1330\]\/60 { background-color: rgba(10, 19, 48, 0.6); }
    .bg-\[\#050a1a\] { background-color: #050a1a; }
    .bg-amber-400\/10 { background-color: rgba(251, 191, 36, 0.1); }
    .bg-amber-400\/25 { background-color: rgba(251, 191, 36, 0.25); }
    .bg-amber-400\/5 { background-color: rgba(251, 191, 36, 0.05); }
    .bg-amber-400\/\[0\.06\] { background-color: rgba(251, 191, 36, 0.06); }
    .bg-red-500 { background-color: #ef4444; }
    .bg-red-500\/15 { background-color: rgba(239, 68, 68, 0.15); }
    .bg-indigo-600\/20 { background-color: rgba(79, 70, 229, 0.2); }

    .border { border-width: 1px; border-style: solid; }
    .border-y { border-top-width: 1px; border-bottom-width: 1px; border-style: solid; }
    .border-b { border-bottom-width: 1px; border-style: solid; }
    .border-t { border-top-width: 1px; border-style: solid; }

    .border-amber-400\/15 { border-color: rgba(251, 191, 36, 0.15); }
    .border-amber-400\/20 { border-color: rgba(251, 191, 36, 0.2); }
    .border-amber-400\/25 { border-color: rgba(251, 191, 36, 0.25); }
    .border-amber-400\/30 { border-color: rgba(251, 191, 36, 0.3); }
    .border-amber-400\/60 { border-color: rgba(251, 191, 36, 0.6); }
    .border-red-500\/40 { border-color: rgba(239, 68, 68, 0.4); }
    .border-white\/5 { border-color: rgba(255, 255, 255, 0.05); }

    .rounded-lg { border-radius: 0.5rem; }
    .rounded-xl { border-radius: 0.75rem; }
    .rounded-2xl { border-radius: 1rem; }
    .rounded-3xl { border-radius: 1.5rem; }
    .rounded-full { border-radius: 9999px; }

    .shadow-lg {
      box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
    }
    .shadow-xl {
      box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
    }
    .shadow-2xl {
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    }

    .overflow-hidden { overflow: hidden; }
    .overflow-x-clip { overflow-x: clip; }
    .whitespace-nowrap { white-space: nowrap; }
    .shrink-0 { flex-shrink: 0; }
    .flex-1 { flex: 1 1 0%; }
    .min-w-0 { min-width: 0; }
    .w-full { width: 100%; }
    .h-px { height: 1px; }
    .h-10 { height: 2.5rem; }
    .h-11 { height: 2.75rem; }
    .h-12 { height: 3rem; }
    .h-14 { height: 3.5rem; }
    .w-10 { width: 2.5rem; }
    .w-11 { width: 2.75rem; }
    .w-12 { width: 3rem; }
    .w-14 { width: 3.5rem; }
    .w-5 { width: 1.25rem; }
    .h-5 { height: 1.25rem; }
    .w-6 { width: 1.5rem; }
    .h-6 { height: 1.5rem; }
    .w-7 { width: 1.75rem; }
    .h-7 { height: 1.75rem; }
    .w-4 { width: 1rem; }
    .h-4 { height: 1rem; }
    .w-3\.5 { width: 0.875rem; }
    .h-3\.5 { height: 0.875rem; }
    .w-3 { width: 0.75rem; }
    .h-3 { height: 0.75rem; }
    .w-2\.5 { width: 0.625rem; }
    .h-2\.5 { height: 0.625rem; }
    .w-2 { width: 0.5rem; }
    .h-2 { height: 0.5rem; }
    .w-1\.5 { width: 0.375rem; }
    .h-1\.5 { height: 0.375rem; }

    /* ===== Sticky / position ===== */
    .sticky { position: sticky; }
    .relative { position: relative; }
    .absolute { position: absolute; }
    .fixed { position: fixed; }
    .inset-0 { inset: 0; }
    .top-0 { top: 0; }
    .top-4 { top: 1rem; }
    .right-0 { right: 0; }
    .right-4 { right: 1rem; }
    .-top-32 { top: -8rem; }
    .-left-24 { left: -6rem; }
    .-right-24 { right: -6rem; }
    .top-40 { top: 10rem; }
    .top-64 { top: 16rem; }
    .left-1\/2 { left: 50%; }
    .-translate-x-1\/2 { transform: translateX(-50%); }
    .z-10 { z-index: 10; }
    .z-40 { z-index: 40; }

    .pointer-events-none { pointer-events: none; }
    .select-none { user-select: none; }
    .outline-none { outline: none; }
    .blur-\[110px\] { filter: blur(110px); }
    .blur-\[120px\] { filter: blur(120px); }
    .blur-\[130px\] { filter: blur(130px); }
    .backdrop-blur-xl { backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); }
    .backdrop-blur-\[18px\] { backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px); }

    /* ===== Hover ===== */
    .transition-all { transition: all 0.3s ease; }
    .transition-colors { transition: color, background-color, border-color 0.2s ease; }
    .transition-transform { transition: transform 0.2s ease; }
    .duration-300 { transition-duration: 0.3s; }
    .duration-500 { transition-duration: 0.5s; }

    .hover\:brightness-110:hover { filter: brightness(1.1); }
    .hover\:border-amber-400\/45:hover { border-color: rgba(251, 191, 36, 0.45); }
    .hover\:border-amber-400\/50:hover { border-color: rgba(251, 191, 36, 0.5); }
    .hover\:border-amber-400\/60:hover { border-color: rgba(251, 191, 36, 0.6); }
    .hover\:bg-amber-400\/10:hover { background-color: rgba(251, 191, 36, 0.1); }
    .hover\:bg-white\/5:hover { background-color: rgba(255, 255, 255, 0.05); }
    .hover\:-translate-y-0\.5:hover { transform: translateY(-0.125rem); }
    .hover\:-translate-y-1:hover { transform: translateY(-0.25rem); }
    .hover\:-translate-y-1\.5:hover { transform: translateY(-0.375rem); }

    .group:hover .group-hover\:translate-x-1 { transform: translateX(0.25rem); }
    .group:hover .group-hover\:translate-x-0\.5 { transform: translateX(0.125rem); }
    .group:hover .group-hover\:-translate-y-0\.5 { transform: translateY(-0.125rem); }
    .group:hover .group-hover\:scale-110 { transform: scale(1.1); }
    .group:hover .group-hover\:text-amber-200 { color: #fde68a; }
    .group:hover .group-hover\:bg-amber-400\/20 { background-color: rgba(251, 191, 36, 0.2); }

    .active\:scale-95:active { transform: scale(0.95); }
    .scale-\[1\.02\] { transform: scale(1.02); }
    .scale-\[1\.04\] { transform: scale(1.04); }

    /* ===== Misc ===== */
    .line-clamp-2 {
      overflow: hidden;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 2;
    }

    .tracking-\[0\.16em\] { letter-spacing: 0.16em; }
    .tracking-\[0\.18em\] { letter-spacing: 0.18em; }
    .tracking-\[0\.22em\] { letter-spacing: 0.22em; }
    .tracking-\[0\.2em\] { letter-spacing: 0.2em; }

    /* ===== Specific components ===== */
    .hero-input::placeholder {
      color: var(--slate-500);
    }

    .ticker-wrap {
      overflow: hidden;
      flex: 1;
      position: relative;
    }

    .live-badge {
      background: linear-gradient(to right, var(--amber-500), var(--amber-600));
      color: var(--navy-800);
      font-weight: 700;
      font-size: 0.6875rem;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      padding: 0.5rem 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      z-index: 10;
    }

    @media (min-width: 640px) {
      .live-badge {
        font-size: 0.75rem;
        padding: 0.5rem 1.25rem;
      }
    }

    .ticker-item {
      margin: 0 1.5rem;
      font-size: 0.75rem;
      color: var(--slate-300);
    }

    @media (min-width: 640px) {
      .ticker-item { font-size: 0.8125rem; }
    }

    .stat-card {
      background: linear-gradient(145deg, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0.025));
      border: 1px solid rgba(212, 175, 55, 0.16);
      border-radius: 1rem;
      padding: 1rem 0.5rem;
      text-align: center;
    }

    .category-btn {
      background: linear-gradient(145deg, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0.025));
      border: 1px solid rgba(212, 175, 55, 0.16);
      border-radius: 1.5rem;
      padding: 1.25rem 1rem;
      text-align: left;
      transition: all 0.3s ease;
      cursor: pointer;
      color: inherit;
      font: inherit;
    }

    @media (min-width: 640px) {
      .category-btn { padding: 1.75rem; }
    }

    .category-btn.active {
      background: linear-gradient(to bottom right, rgba(251, 191, 36, 0.25), rgba(217, 119, 6, 0.1));
      border-color: rgba(251, 191, 36, 0.6);
      box-shadow: 0 20px 25px -5px rgba(245, 158, 11, 0.1);
      transform: scale(1.02);
    }

    .category-btn:hover:not(.active) {
      border-color: rgba(251, 191, 36, 0.45);
      transform: translateY(-0.25rem);
    }

    .category-icon {
      width: 2.75rem;
      height: 2.75rem;
      border-radius: 0.75rem;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 0.75rem;
      transition: all 0.3s ease;
    }

    @media (min-width: 640px) {
      .category-icon { width: 3.5rem; height: 3.5rem; margin-bottom: 1rem; }
    }

    .category-btn.active .category-icon {
      background: linear-gradient(to bottom right, var(--amber-300), var(--amber-600));
    }

    .category-btn:not(.active) .category-icon {
      background: rgba(251, 191, 36, 0.1);
      border: 1px solid rgba(251, 191, 36, 0.25);
    }

    .category-btn:hover:not(.active) .category-icon {
      background: rgba(251, 191, 36, 0.2);
    }

    .term-card {
      background: linear-gradient(145deg, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0.025));
      border: 1px solid rgba(212, 175, 55, 0.16);
      border-radius: 1rem;
      padding: 1.25rem;
      text-align: left;
      cursor: pointer;
      transition: all 0.3s ease;
      color: inherit;
      font: inherit;
    }

    .term-card:hover {
      border-color: rgba(251, 191, 36, 0.5);
      transform: translateY(-0.125rem);
    }

    .news-card {
      background: linear-gradient(145deg, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0.025));
      border: 1px solid rgba(212, 175, 55, 0.16);
      border-radius: 1rem;
      padding: 1.25rem;
      transition: all 0.3s ease;
      position: relative;
    }

    .news-card:hover {
      border-color: rgba(251, 191, 36, 0.45);
    }

    .link-card {
      background: linear-gradient(145deg, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0.025));
      border: 1px solid rgba(212, 175, 55, 0.16);
      border-radius: 1.5rem;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      transition: all 0.3s ease;
      text-decoration: none;
      color: inherit;
    }

    .link-card:hover {
      border-color: rgba(251, 191, 36, 0.5);
      transform: translateY(-0.375rem);
    }

    .link-card .link-icon {
      width: 3rem;
      height: 3rem;
      border-radius: 1rem;
      background: linear-gradient(to bottom right, var(--amber-300), var(--amber-600));
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 1.25rem;
      box-shadow: 0 10px 15px -3px rgba(245, 158, 11, 0.2);
      transition: transform 0.3s ease;
    }

    .link-card:hover .link-icon {
      transform: scale(1.1);
    }

    .explainer-panel {
      background: linear-gradient(145deg, rgba(20, 30, 60, 0.85), rgba(10, 16, 36, 0.92));
      border: 1px solid rgba(212, 175, 55, 0.22);
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
      border-radius: 1.5rem;
      overflow: hidden;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
      transition: opacity 0.5s ease, transform 0.5s ease;
    }

    .explainer-panel.visible {
      opacity: 1;
      transform: translateY(0);
    }

    .explainer-panel.hidden {
      opacity: 0;
      transform: translateY(1.5rem);
    }

    .explainer-header {
      background: linear-gradient(to right, rgba(251, 191, 36, 0.2), rgba(245, 158, 11, 0.1), transparent);
      border-bottom: 1px solid rgba(251, 191, 36, 0.2);
      padding: 1.5rem 1.5rem;
    }

    @media (min-width: 640px) {
      .explainer-header { padding: 2rem 2.5rem; }
    }

    .step-number {
      width: 1.75rem;
      height: 1.75rem;
      border-radius: 9999px;
      background: linear-gradient(to bottom right, var(--amber-300), var(--amber-600));
      color: var(--navy-800);
      font-size: 0.75rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 0.125rem;
    }

    .info-box {
      border: 1px solid rgba(251, 191, 36, 0.2);
      background: rgba(251, 191, 36, 0.06);
      border-radius: 1rem;
      padding: 1rem 1.25rem;
    }

    .btn-gold {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      padding: 0.625rem 1.5rem;
      border-radius: 9999px;
      background: linear-gradient(to right, var(--amber-400), var(--amber-600));
      color: var(--navy-800);
      font-weight: 700;
      font-size: 0.875rem;
      box-shadow: 0 10px 15px -3px rgba(245, 158, 11, 0.25);
      transition: all 0.2s ease;
      border: none;
      cursor: pointer;
      text-decoration: none;
    }

    .btn-gold:hover {
      filter: brightness(1.1);
    }

    .btn-gold:active {
      transform: scale(0.95);
    }

    .btn-glass {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      padding: 0.625rem 1.25rem;
      border-radius: 9999px;
      background: linear-gradient(145deg, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0.025));
      border: 1px solid rgba(212, 175, 55, 0.2);
      color: var(--amber-200);
      font-weight: 600;
      font-size: 0.875rem;
      transition: all 0.2s ease;
      cursor: pointer;
      text-decoration: none;
    }

    .btn-glass:hover {
      border-color: rgba(251, 191, 36, 0.6);
      background: rgba(251, 191, 36, 0.1);
    }

    .btn-glass:active {
      transform: scale(0.95);
    }

    /* ===== Language toggle ===== */
    .lang-toggle {
      display: flex;
      align-items: center;
      gap: 0.375rem;
      padding: 0.5rem 0.75rem;
      border-radius: 9999px;
      background: linear-gradient(145deg, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0.025));
      border: 1px solid rgba(212, 175, 55, 0.16);
      color: #fde68a;
      font-size: 0.75rem;
      font-weight: 600;
      transition: all 0.2s ease;
      cursor: pointer;
    }

    .lang-toggle:hover {
      border-color: rgba(251, 191, 36, 0.5);
    }

    /* ===== Responsive tweaks ===== */
    @media (max-width: 640px) {
      .category-btn .cat-title { font-size: 1rem; }
      .category-btn .cat-sub { font-size: 0.6875rem; }
    }

    /* ===== Google search bar ===== */
    .google-bar {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      max-width: 36rem;
      margin: 0 auto;
    }

    @media (min-width: 640px) {
      .google-bar { flex-direction: row; }
    }

    /* ===== Footer ===== */
    .footer-gold {
      color: var(--gold);
    }
  </style>
</head>
<body>

  <!-- ===== ROOT ===== -->
  <div id="app"></div>

  <script>
    // ============================================================
    //  DATA & TRANSLATIONS
    // ============================================================

    const CATEGORIES = [
      { id: "criminal", label: "Criminal", labelKn: "ಕ್ರಿಮಿನಲ್", tagline: "FIR, bail, warrants & police matters", taglineKn: "FIR, ಜಾಮೀನು, ವಾರಂಟ್ ಮತ್ತು ಪೊಲೀಸ್ ವಿಷಯಗಳು", icon: "ShieldAlert" },
      { id: "civil", label: "Civil", labelKn: "ಸಿವಿಲ್", tagline: "Money recovery, cheques & court suits", taglineKn: "ಹಣ ವಸೂಲಿ, ಚೆಕ್ ಮತ್ತು ನ್ಯಾಯಾಲಯದ ದಾವೆಗಳು", icon: "FileText" },
      { id: "family", label: "Family", labelKn: "ಕುಟುಂಬ", tagline: "Divorce, custody & maintenance", taglineKn: "ವಿಚ್ಛೇದನ, ಪಾಲನೆ ಮತ್ತು ಜೀವನಾಂಶ", icon: "Users" },
      { id: "property", label: "Property", labelKn: "ಆಸ್ತಿ", tagline: "Land disputes, tenancy & registration", taglineKn: "ಭೂ ವಿವಾದ, ಬಾಡಿಗೆ ಮತ್ತು ನೋಂದಣಿ", icon: "Home" },
      { id: "cyber", label: "Cyber Crime", labelKn: "ಸೈಬರ್ ಅಪರಾಧ", tagline: "Online fraud, hacking & reporting", taglineKn: "ಆನ್‌ಲೈನ್ ವಂಚನೆ, ಹ್ಯಾಕಿಂಗ್ ಮತ್ತು ದೂರು", icon: "Cpu" },
      { id: "consumer", label: "Consumer", labelKn: "ಗ್ರಾಹಕ", tagline: "Refunds, defects & e-Daakhil complaints", taglineKn: "ಮರುಪಾವತಿ, ದೋಷಗಳು ಮತ್ತು ಇ-ದಾಖಿಲ್ ದೂರುಗಳು", icon: "ShoppingBag" }
    ];

    const TERMS = [
      {
        id: "fir", name: "FIR (First Information Report)", nameKn: "FIR (ಪ್ರಥಮ ಮಾಹಿತಿ ವರದಿ)", category: "criminal",
        keywords: ["fir", "first information report", "police complaint", "complaint", "police", "report crime"],
        meaning: "An FIR is the written record the police make when you report a serious (cognizable) crime like theft, assault or fraud. Once registered, the police must investigate. You are entitled to a free copy, and the FIR gets a number you can track online.",
        meaningKn: "ಕಳ್ಳತನ, ಹಲ್ಲೆ ಅಥವಾ ವಂಚನೆಯಂತಹ ಗಂಭೀರ ಅಪರಾಧವನ್ನು ನೀವು ವರದಿ ಮಾಡಿದಾಗ ಪೊಲೀಸರು ಮಾಡುವ ಲಿಖಿತ ದಾಖಲೆಯೇ FIR. ನೋಂದಣಿಯಾದ ನಂತರ ಪೊಲೀಸರು ತನಿಖೆ ನಡೆಸಬೇಕು. ನಿಮಗೆ ಉಚಿತ ಪ್ರತಿಯ ಹಕ್ಕಿದೆ ಮತ್ತು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಟ್ರ್ಯಾಕ್ ಮಾಡಬಹುದಾದ ಸಂಖ್ಯೆ ಸಿಗುತ್ತದೆ.",
        steps: ["Go to the nearest police station (or use your state's online citizen portal)", "Give your complaint in writing, or dictate it — the officer must write it down", "Read it carefully, sign it, and take your free signed copy with the FIR number", "The police begin investigation and file a chargesheet in court"],
        time: "Registered the same day · Investigation usually 60–90 days", timeKn: "ಅದೇ ದಿನ ನೋಂದಣಿ · ತನಿಖೆ ಸಾಮಾನ್ಯವಾಗಿ 60–90 ದಿನಗಳು",
        cost: "Completely free — no fee to file an FIR", costKn: "ಸಂಪೂರ್ಣ ಉಚಿತ — FIR ದಾಖಲಿಸಲು ಯಾವುದೇ ಶುಲ್ಕವಿಲ್ಲ"
      },
      {
        id: "bail", name: "Bail", nameKn: "ಜಾಮೀನು", category: "criminal",
        keywords: ["bail", "jamin", "bail application", "release", "regular bail", "station bail", "surety"],
        meaning: "Bail is the court's permission for an arrested person to stay out of jail while the trial continues. The court usually asks for a surety (a person who guarantees you) and a bond amount, which is refunded after the trial if you attend all hearings.",
        meaningKn: "ವಿಚಾರಣೆ ಮುಂದುವರಿದಿರುವಾಗ ಬಂಧಿತ ವ್ಯಕ್ತಿ ಜೈಲಿನ ಹೊರಗೆ ಇರಲು ನ್ಯಾಯಾಲಯ ನೀಡುವ ಅನುಮತಿಯೇ ಜಾಮೀನು. ನ್ಯಾಯಾಲಯ ಸಾಮಾನ್ಯವಾಗಿ ಜಾಮೀನುದಾರ ಮತ್ತು ಬಾಂಡ್ ಮೊತ್ತವನ್ನು ಕೇಳುತ್ತದೆ; ಎಲ್ಲಾ ವಿಚಾರಣೆಗಳಿಗೆ ಹಾಜರಾದರೆ ವಿಚಾರಣೆಯ ನಂತರ ಮೊತ್ತ ಮರಳಿ ಸಿಗುತ್ತದೆ.",
        steps: ["A lawyer files a bail application in the concerned court", "The court hears arguments from both sides", "The judge sets conditions — surety, bond amount, passport surrender etc.", "Deposit the bond and complete surety formalities", "The accused is released from custody"],
        time: "Station bail: same day · Regular bail: 1 day – 2 weeks", timeKn: "ಠಾಣಾ ಜಾಮೀನು: ಅದೇ ದಿನ · ಸಾಮಾನ್ಯ ಜಾಮೀನು: 1 ದಿನ – 2 ವಾರಗಳು",
        cost: "Lawyer fees ₹5,000 – ₹50,000+ · Bond amount is refunded after trial", costKn: "ವಕೀಲರ ಶುಲ್ಕ ₹5,000 – ₹50,000+ · ವಿಚಾರಣೆಯ ನಂತರ ಬಾಂಡ್ ಮೊತ್ತ ಮರಳುತ್ತದೆ"
      },
      {
        id: "anticipatory-bail", name: "Anticipatory Bail", nameKn: "ಮುಂಗಡ ಜಾಮೀನು", category: "criminal",
        keywords: ["anticipatory", "advance bail", "pre arrest", "438"],
        meaning: "Anticipatory bail is protection from arrest before it happens — you ask the court in advance that if the police come to arrest you, you should be released on bail immediately. It is filed in the Sessions Court or High Court.",
        meaningKn: "ಬಂಧನವಾಗುವ ಮೊದಲೇ ಪಡೆಯುವ ರಕ್ಷಣೆಯೇ ಮುಂಗಡ ಜಾಮೀನು — ಪೊಲೀಸರು ಬಂಧಿಸಲು ಬಂದರೆ ತಕ್ಷಣ ಜಾಮೀನಿನಲ್ಲಿ ಬಿಡುಗಡೆ ಮಾಡಬೇಕೆಂದು ನ್ಯಾಯಾಲಯವನ್ನು ಮುಂಚಿತವಾಗಿ ಕೇಳುವುದು. ಇದನ್ನು ಸೆಷನ್ಸ್ ನ್ಯಾಯಾಲಯ ಅಥವಾ ಹೈಕೋರ್ಟ್‌ನಲ್ಲಿ ಸಲ್ಲಿಸಲಾಗುತ್ತದೆ.",
        steps: ["Lawyer files the application in the Sessions Court or High Court", "Court may grant interim protection from arrest", "Notice is issued to the police / prosecution for their reply", "After hearing, the court grants bail with conditions", "Surrender before the court or investigating officer as directed"],
        time: "Usually 1 – 4 weeks", timeKn: "ಸಾಮಾನ್ಯವಾಗಿ 1 – 4 ವಾರಗಳು",
        cost: "Lawyer fees ₹15,000 – ₹1,00,000+", costKn: "ವಕೀಲರ ಶುಲ್ಕ ₹15,000 – ₹1,00,000+"
      },
      {
        id: "summons", name: "Court Summons", nameKn: "ನ್ಯಾಯಾಲಯದ ಸಮನ್ಸ್", category: "criminal",
        keywords: ["summons", "court notice", "notice", "summon"],
        meaning: "A summons is a court order asking you to appear before it on a fixed date — as a witness, accused or party to a case. Ignoring a summons can lead to a warrant, so always note the date and respond.",
        meaningKn: "ಸಾಕ್ಷಿ, ಆರೋಪಿ ಅಥವಾ ಪ್ರಕರಣದ ಪಕ್ಷವಾಗಿ ನಿಗದಿತ ದಿನಾಂಕದಂದು ಹಾಜರಾಗುವಂತೆ ಕೇಳುವ ನ್ಯಾಯಾಲಯದ ಆದೇಶವೇ ಸಮನ್ಸ್. ಸಮನ್ಸ್ ಅನ್ನು ನಿರ್ಲಕ್ಷಿಸಿದರೆ ವಾರಂಟ್ ಬರಬಹುದು, ಆದ್ದರಿಂದ ದಿನಾಂಕವನ್ನು ಗಮನಿಸಿ ಪ್ರತಿಕ್ರಿಯಿಸಿ.",
        steps: ["Receive the summons and note the date, time and court room", "Appear in person, or send your lawyer if permitted", "Carry an ID and any documents mentioned", "Follow the judge's directions on the next date"],
        time: "Arrives within days of issue · Attend on the date given", timeKn: "ಜಾರಿಯಾದ ಕೆಲವು ದಿನಗಳಲ್ಲಿ ಬರುತ್ತದೆ · ನೀಡಿದ ದಿನಾಂಕದಂದು ಹಾಜರಾಗಿ",
        cost: "No fee to receive · Lawyer fees only if you hire one", costKn: "ಸ್ವೀಕರಿಸಲು ಶುಲ್ಕವಿಲ್ಲ · ವಕೀಲರನ್ನು ನೇಮಿಸಿದರೆ ಮಾತ್ರ ಶುಲ್ಕ"
      },
      {
        id: "arrest-warrant", name: "Arrest Warrant", nameKn: "ಬಂಧನ ವಾರಂಟ್", category: "criminal",
        keywords: ["warrant", "arrest warrant", "non bailable warrant", "nbw"],
        meaning: "An arrest warrant is a judge's written order authorising the police to arrest a person and bring them to court — usually issued when someone ignores summons or is evading the case. A bailable warrant lets you get bail at the police station; a non-bailable one means you must go before the judge.",
        meaningKn: "ವ್ಯಕ್ತಿಯನ್ನು ಬಂಧಿಸಿ ನ್ಯಾಯಾಲಯಕ್ಕೆ ಹಾಜರುಪಡಿಸಲು ಪೊಲೀಸರಿಗೆ ಅಧಿಕಾರ ನೀಡುವ ನ್ಯಾಯಾಧೀಶರ ಲಿಖಿತ ಆದೇಶವೇ ಬಂಧನ ವಾರಂಟ್.",
        steps: ["Warrant is issued by the magistrate / judge", "Police execute it and arrest the person", "The person must be produced before a magistrate within 24 hours", "Bail or remand hearing happens immediately"],
        time: "Can be executed any time after it is issued", timeKn: "ಜಾರಿಯಾದ ನಂತರ ಯಾವುದೇ ಸಮಯದಲ್ಲಿ ಜಾರಿಗೊಳಿಸಬಹುದು",
        cost: "Lawyer fees ₹10,000+ to seek recall / cancellation", costKn: "ರದ್ದತಿ / ಹಿಂಪಡೆಯಲು ವಕೀಲರ ಶುಲ್ಕ ₹10,000+"
      },
      {
        id: "cheque-bounce", name: "Cheque Bounce (Section 138)", nameKn: "ಚೆಕ್ ಬೌನ್ಸ್ (ಸೆಕ್ಷನ್ 138)", category: "civil",
        keywords: ["cheque bounce", "138", "ni act", "bounced cheque", "check bounce"],
        meaning: "When a cheque bounces due to insufficient funds, it is a criminal offence under Section 138 of the Negotiable Instruments Act. The payee can send a legal notice and, if unpaid, file a criminal complaint — punishable with up to 2 years in jail or a fine.",
        meaningKn: "ಸಾಕಷ್ಟು ಹಣವಿಲ್ಲದೆ ಚೆಕ್ ಬೌನ್ಸ್ ಆದರೆ, ನೆಗೋಷಿಯಬಲ್ ಇನ್‌ಸ್ಟ್ರುಮೆಂಟ್ಸ್ ಕಾಯ್ದೆಯ ಸೆಕ್ಷನ್ 138 ರ ಅಡಿಯಲ್ಲಿ ಅದು ಕ್ರಿಮಿನಲ್ ಅಪರಾಧ.",
        steps: ["Send a written demand notice within 30 days of the bounce", "Give the drawer 15 days to pay after receiving the notice", "If unpaid, file a complaint in court within the next 30 days", "Trial proceeds — most cases settle with payment + compensation"],
        time: "Typically 6 months – 2 years", timeKn: "ಸಾಮಾನ್ಯವಾಗಿ 6 ತಿಂಗಳು – 2 ವರ್ಷಗಳು",
        cost: "Lawyer fees ₹10,000 – ₹50,000+", costKn: "ವಕೀಲರ ಶುಲ್ಕ ₹10,000 – ₹50,000+"
      },
      {
        id: "money-recovery", name: "Money Recovery Suit", nameKn: "ಹಣ ವಸೂಲಿ ದಾವೆ", category: "civil",
        keywords: ["money recovery", "civil suit", "loan recovery", "debt", "recovery suit"],
        meaning: "If someone owes you money and refuses to pay, you can file a civil suit for recovery in court. You need proof — loan agreement, bank transfers, messages or witnesses. The court can order payment with interest and attach the debtor's property if they don't comply.",
        meaningKn: "ಯಾರಾದರೂ ನಿಮಗೆ ಹಣ ಕೊಡಬೇಕಿದ್ದು ಪಾವತಿಸಲು ನಿರಾಕರಿಸಿದರೆ, ನ್ಯಾಯಾಲಯದಲ್ಲಿ ಹಣ ವಸೂಲಿಗಾಗಿ ಸಿವಿಲ್ ದಾವೆ ಹೂಡಬಹುದು.",
        steps: ["Send a legal notice demanding payment within a deadline", "File the suit in the civil court with all proof attached", "Both sides present evidence and arguments", "Court passes a judgment (decree) for payment", "If unpaid, enforce the decree — property can be attached"],
        time: "Usually 1 – 3 years", timeKn: "ಸಾಮಾನ್ಯವಾಗಿ 1 – 3 ವರ್ಷಗಳು",
        cost: "Court fee based on claim amount + lawyer fees", costKn: "ಹಕ್ಕು ಮೊತ್ತದ ಆಧಾರದ ಮೇಲೆ ನ್ಯಾಯಾಲಯ ಶುಲ್ಕ + ವಕೀಲರ ಶುಲ್ಕ"
      },
      {
        id: "divorce", name: "Divorce", nameKn: "ವಿಚ್ಛೇದನ", category: "family",
        keywords: ["divorce", "talaq", "mutual divorce", "separation", "divorce process"],
        meaning: "Divorce is the legal end of a marriage granted by a family court. Mutual-consent divorce (both partners agree) is faster and simpler; a contested divorce (one side disagrees) takes longer. The court also settles alimony, child custody and property division.",
        meaningKn: "ಕುಟುಂಬ ನ್ಯಾಯಾಲಯ ನೀಡುವ ಮದುವೆಯ ಕಾನೂನುಬದ್ಧ ಅಂತ್ಯವೇ ವಿಚ್ಛೇದನ.",
        steps: ["File a divorce petition (joint for mutual, single for contested)", "Attend court counselling / mediation sessions", "Mutual cases have a cooling period (often waived by courts now)", "Agree on alimony, custody and property terms", "Court grants the divorce decree"],
        time: "Mutual: 6 – 12 months · Contested: 2 – 5 years", timeKn: "ಪರಸ್ಪರ: 6 – 12 ತಿಂಗಳು · ವಿವಾದಿತ: 2 – 5 ವರ್ಷಗಳು",
        cost: "₹25,000 – ₹2,00,000+ depending on complexity", costKn: "ಸಂಕೀರ್ಣತೆಯನ್ನು ಅವಲಂಬಿಸಿ ₹25,000 – ₹2,00,000+"
      },
      {
        id: "alimony", name: "Alimony / Maintenance", nameKn: "ಜೀವನಾಂಶ / ನಿರ್ವಹಣಾ ಭತ್ಯೆ", category: "family",
        keywords: ["alimony", "maintenance", "monthly maintenance", "125 crpc", "spouse support"],
        meaning: "Alimony (maintenance) is financial support a court orders one spouse to pay the other after separation or divorce — to cover living expenses. The amount depends on income, lifestyle and needs, and courts can grant interim (temporary) maintenance quickly.",
        meaningKn: "ಬೇರ್ಪಡೆ ಅಥವಾ ವಿಚ್ಛೇದನದ ನಂತರ ಜೀವನ ವೆಚ್ಚಕ್ಕಾಗಿ ಒಂದು ಸಂಗಾತಿ ಇನ್ನೊಬ್ಬರಿಗೆ ಪಾವತಿಸಬೇಕೆಂದು ನ್ಯಾಯಾಲಯ ಆದೇಶಿಸುವ ಆರ್ಥಿಕ ನೆರವೇ ಜೀವನಾಂಶ.",
        steps: ["File a maintenance petition in the family court", "Court assesses both sides' income and expenses", "Interim maintenance can be ordered within weeks", "Final order fixes the monthly amount", "Non-payment can be enforced through the court"],
        time: "Interim: 1 – 3 months · Final: 6 – 18 months", timeKn: "ಮಧ್ಯಂತರ: 1 – 3 ತಿಂಗಳು · ಅಂತಿಮ: 6 – 18 ತಿಂಗಳು",
        cost: "Lawyer fees ₹10,000 – ₹50,000 · Amount depends on income", costKn: "ವಕೀಲರ ಶುಲ್ಕ ₹10,000 – ₹50,000 · ಮೊತ್ತ ಆದಾಯವನ್ನು ಅವಲಂಬಿಸಿರುತ್ತದೆ"
      },
      {
        id: "domestic-violence", name: "Domestic Violence Protection", nameKn: "ಕೌಟುಂಬಿಕ ಹಿಂಸೆ ರಕ್ಷಣೆ", category: "family",
        keywords: ["domestic violence", "dv act", "protection order", "abuse", "harassment wife"],
        meaning: "The Protection of Women from Domestic Violence Act, 2005 protects women from physical, verbal, emotional, sexual or economic abuse at home. You can get a protection order, residence rights and monetary relief — and free help is available through Protection Officers and NALSA legal aid.",
        meaningKn: "ಕೌಟುಂಬಿಕ ಹಿಂಸೆಯಿಂದ ಮಹಿಳೆಯರ ರಕ್ಷಣಾ ಕಾಯ್ದೆ, 2005 ಮನೆಯಲ್ಲಿ ದೈಹಿಕ, ಮೌಖಿಕ, ಭಾವನಾತ್ಮಕ, ಲೈಂಗಿಕ ಅಥವಾ ಆರ್ಥಿಕ ದೌರ್ಜನ್ಯದಿಂದ ಮಹಿಳೆಯರನ್ನು ರಕ್ಷಿಸುತ್ತದೆ.",
        steps: ["Complain to the police, a Protection Officer, or directly to the magistrate", "Ask for an interim protection order — granted within days", "Attend the hearing with your evidence", "Court can order residence rights, maintenance and compensation", "Violation of the order is punishable"],
        time: "Protection order: within days · Full case: 6 – 12 months", timeKn: "ರಕ್ಷಣಾ ಆದೇಶ: ಕೆಲವು ದಿನಗಳಲ್ಲಿ · ಪೂರ್ಣ ಪ್ರಕರಣ: 6 – 12 ತಿಂಗಳು",
        cost: "Free via Protection Officer · NALSA legal aid available", costKn: "ರಕ್ಷಣಾ ಅಧಿಕಾರಿ ಮೂಲಕ ಉಚಿತ · NALSA ಕಾನೂನು ನೆರವು ಲಭ್ಯ"
      },
      {
        id: "child-custody", name: "Child Custody", nameKn: "ಮಕ್ಕಳ ಪಾಲನೆ", category: "family",
        keywords: ["custody", "child custody", "visitation", "guardian", "child"],
        meaning: "When parents separate, the court decides who the child lives with (custody) and how the other parent stays in touch (visitation). The single most important factor is the child's welfare — not automatically the father or the mother.",
        meaningKn: "ಪೋಷಕರು ಬೇರ್ಪಟ್ಟಾಗ ಮಗು ಯಾರೊಂದಿಗೆ ವಾಸಿಸಬೇಕು (ಪಾಲನೆ) ಮತ್ತು ಇನ್ನೊಬ್ಬ ಪೋಷಕರು ಹೇಗೆ ಸಂಪರ್ಕದಲ್ಲಿರಬೇಕು (ಭೇಟಿ ಹಕ್ಕು) ಎಂದು ನ್ಯಾಯಾಲಯ ನಿರ್ಧರಿಸುತ್ತದೆ.",
        steps: ["File a custody petition in the family court", "Attend mediation to try an amicable arrangement", "Court considers the child's age, welfare and wishes", "Interim custody / visitation is fixed early", "Final custody order is passed"],
        time: "Usually 6 months – 2 years", timeKn: "ಸಾಮಾನ್ಯವಾಗಿ 6 ತಿಂಗಳು – 2 ವರ್ಷಗಳು",
        cost: "Lawyer fees ₹20,000 – ₹1,00,000+", costKn: "ವಕೀಲರ ಶುಲ್ಕ ₹20,000 – ₹1,00,000+"
      },
      {
        id: "property-dispute", name: "Property / Land Dispute", nameKn: "ಆಸ್ತಿ / ಭೂ ವಿವಾದ", category: "property",
        keywords: ["property", "land dispute", "partition", "title", "ownership", "boundary"],
        meaning: "Property disputes arise over ownership, boundaries, possession or inheritance of land and houses. The golden rule: the person with clear, registered title documents usually wins. Always verify title, check for loans/mortgages, and get an encumbrance certificate before buying.",
        meaningKn: "ಭೂಮಿ ಮತ್ತು ಮನೆಗಳ ಮಾಲೀಕತ್ವ, ಗಡಿ, ಸ್ವಾಧೀನ ಅಥವಾ ಉತ್ತರಾಧಿಕಾರದ ಬಗ್ಗೆ ಆಸ್ತಿ ವಿವಾದಗಳು ಉದ್ಭವಿಸುತ್ತವೆ. ಸುವರ್ಣ ನಿಯಮ: ಸ್ಪಷ್ಟ, ನೋಂದಾಯಿತ ಮಾಲೀಕತ್ವ ದಾಖಲೆಗಳಿರುವ ವ್ಯಕ್ತಿ ಸಾಮಾನ್ಯವಾಗಿ ಗೆಲ್ಲುತ್ತಾರೆ.",
        steps: ["Collect and verify all title documents (sale deed, khata, EC)", "Send a legal notice to the other party", "File a civil suit (declaration / partition / injunction)", "Both sides present documents, witnesses and arguments", "Court passes a decree; get it executed if needed"],
        time: "Typically 2 – 10 years in civil court", timeKn: "ಸಿವಿಲ್ ನ್ಯಾಯಾಲಯದಲ್ಲಿ ಸಾಮಾನ್ಯವಾಗಿ 2 – 10 ವರ್ಷಗಳು",
        cost: "Court fee ~1–7% of property value + lawyer fees", costKn: "ಆಸ್ತಿ ಮೌಲ್ಯದ ~1–7% ನ್ಯಾಯಾಲಯ ಶುಲ್ಕ + ವಕೀಲರ ಶುಲ್ಕ"
      },
      {
        id: "tenant-eviction", name: "Tenant Eviction", nameKn: "ಬಾಡಿಗೆದಾರರ ತೆರವು", category: "property",
        keywords: ["eviction", "tenant", "rent", "landlord", "tenant removal", "rent control"],
        meaning: "A landlord cannot simply throw a tenant out or cut water/power — eviction must go through the court (or Rent Authority under state Rent Acts). Valid grounds include unpaid rent, misuse of property, or the owner's genuine personal need.",
        meaningKn: "ಮನೆಮಾಲೀಕರು ಬಾಡಿಗೆದಾರರನ್ನು ಸುಮ್ಮನೆ ಹೊರಹಾಕುವಂತಿಲ್ಲ ಅಥವಾ ನೀರು/ವಿದ್ಯುತ್ ಕಡಿತಗೊಳಿಸುವಂತಿಲ್ಲ — ತೆರವು ನ್ಯಾಯಾಲಯದ (ಅಥವಾ ರಾಜ್ಯ ಬಾಡಿಗೆ ಕಾಯ್ದೆಯಡಿ ಬಾಡಿಗೆ ಪ್ರಾಧಿಕಾರ) ಮೂಲಕವೇ ಆಗಬೇಕು.",
        steps: ["Send a legal notice asking the tenant to vacate", "File an eviction petition before the court / Rent Authority", "Attend hearings and prove valid grounds", "Obtain the eviction order", "Get it executed through the court if the tenant doesn't leave"],
        time: "Usually 6 months – 2 years", timeKn: "ಸಾಮಾನ್ಯವಾಗಿ 6 ತಿಂಗಳು – 2 ವರ್ಷಗಳು",
        cost: "Lawyer fees ₹15,000 – ₹75,000+", costKn: "ವಕೀಲರ ಶುಲ್ಕ ₹15,000 – ₹75,000+"
      },
      {
        id: "property-registration", name: "Property Registration", nameKn: "ಆಸ್ತಿ ನೋಂದಣಿ", category: "property",
        keywords: ["registration", "sale deed", "registry", "stamp duty", "sub registrar"],
        meaning: "Registering your property deal at the sub-registrar's office is what makes you the legal owner in government records. You pay stamp duty + registration fee, both parties sign before the registrar, and you receive the registered sale deed.",
        meaningKn: "ಉಪ-ನೋಂದಣಾಧಿಕಾರಿ ಕಚೇರಿಯಲ್ಲಿ ನಿಮ್ಮ ಆಸ್ತಿ ವ್ಯವಹಾರವನ್ನು ನೋಂದಾಯಿಸುವುದೇ ಸರ್ಕಾರಿ ದಾಖಲೆಗಳಲ್ಲಿ ನಿಮ್ಮನ್ನು ಕಾನೂನುಬದ್ಧ ಮಾಲೀಕರನ್ನಾಗಿ ಮಾಡುತ್ತದೆ.",
        steps: ["Draft the sale deed with all details verified", "Pay stamp duty and registration fees (online in most states)", "Book a slot at the sub-registrar office", "Both parties sign with witnesses before the registrar", "Collect the registered deed — ownership is now official"],
        time: "Completed the same day at the registrar office", timeKn: "ನೋಂದಣಾಧಿಕಾರಿ ಕಚೇರಿಯಲ್ಲಿ ಅದೇ ದಿನ ಪೂರ್ಣಗೊಳ್ಳುತ್ತದೆ",
        cost: "Stamp duty 5–7% + registration ~1% (varies by state)", costKn: "ಸ್ಟಾಂಪ್ ಡ್ಯೂಟಿ 5–7% + ನೋಂದಣಿ ~1% (ರಾಜ್ಯವನ್ನು ಅವಲಂಬಿಸಿ)"
      },
      {
        id: "cyber-crime", name: "Cyber Crime Complaint", nameKn: "ಸೈಬರ್ ಅಪರಾಧ ದೂರು", category: "cyber",
        keywords: ["cyber", "online fraud", "phishing", "otp fraud", "hacking", "upi fraud", "scam", "1930"],
        meaning: "Fell for a fake OTP call, UPI fraud or online scam? Call the national helpline 1930 immediately and file a complaint at cybercrime.gov.in. Reporting within the 'golden hours' greatly improves the chance of freezing the fraudster's account and recovering your money.",
        meaningKn: "ನಕಲಿ OTP ಕರೆ, UPI ವಂಚನೆ ಅಥವಾ ಆನ್‌ಲೈನ್ ಮೋಸಕ್ಕೆ ಬಲಿಯಾದಿರಾ? ತಕ್ಷಣ ರಾಷ್ಟ್ರೀಯ ಸಹಾಯವಾಣಿ 1930 ಗೆ ಕರೆ ಮಾಡಿ ಮತ್ತು cybercrime.gov.in ನಲ್ಲಿ ದೂರು ಸಲ್ಲಿಸಿ.",
        steps: ["Call 1930 (national cyber helpline) immediately", "File a complaint at cybercrime.gov.in with screenshots & transaction IDs", "Visit your local cyber cell with ID proof and evidence", "An FIR is registered and investigation begins", "Track your complaint with the acknowledgement number"],
        time: "Report within hours for the best recovery chance", timeKn: "ಉತ್ತಮ ಮರುಪಡೆಯುವಿಕೆಗಾಗಿ ಕೆಲವು ಗಂಟೆಗಳೊಳಗೆ ವರದಿ ಮಾಡಿ",
        cost: "Completely free to report", costKn: "ವರದಿ ಮಾಡಲು ಸಂಪೂರ್ಣ ಉಚಿತ"
      },
      {
        id: "consumer-complaint", name: "Consumer Complaint", nameKn: "ಗ್ರಾಹಕ ದೂರು", category: "consumer",
        keywords: ["consumer", "complaint", "refund", "defective", "e-daakhil", "cheated", "product"],
        meaning: "Cheated by a defective product, poor service or undelivered order? Under the Consumer Protection Act 2019 you can file a complaint in the Consumer Commission — even online via the e-Daakhil portal — and claim refund, replacement or compensation.",
        meaningKn: "ದೋಷಪೂರಿತ ಉತ್ಪನ್ನ, ಕಳಪೆ ಸೇವೆ ಅಥವಾ ತಲುಪದ ಆರ್ಡರ್‌ನಿಂದ ಮೋಸ ಹೋದಿರಾ? ಗ್ರಾಹಕ ರಕ್ಷಣಾ ಕಾಯ್ದೆ 2019 ರ ಅಡಿಯಲ್ಲಿ ಗ್ರಾಹಕ ಆಯೋಗದಲ್ಲಿ ದೂರು ಸಲ್ಲಿಸಬಹುದು — ಇ-ದಾಖಿಲ್ ಪೋರ್ಟಲ್ ಮೂಲಕ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿಯೂ.",
        steps: ["Send a written notice to the seller asking for refund / fix", "File your complaint at edaakhil.nic.in with bills and photos", "Attend the hearing (often via video call)", "The commission orders refund, replacement or compensation"],
        time: "Typically 3 – 12 months", timeKn: "ಸಾಮಾನ್ಯವಾಗಿ 3 – 12 ತಿಂಗಳು",
        cost: "Nominal fee ₹100 – ₹5,000 based on claim value", costKn: "ಹಕ್ಕು ಮೌಲ್ಯದ ಆಧಾರದ ಮೇಲೆ ₹100 – ₹5,000 ನಾಮಮಾತ್ರ ಶುಲ್ಕ"
      }
    ];

    const NEWS = [
      { court: "Supreme Court", title: "Constitution Bench to hear electoral reforms plea next week", detail: "A 5-judge bench will examine fresh guidelines on transparent campaign funding." },
      { court: "Karnataka HC", title: "E-filing made mandatory for all civil cases", detail: "Physical filing counters to close for civil matters from next month; helpdesks at every district court." },
      { court: "Delhi HC", title: "Court directs speedy trial in 10-year-old property dispute", detail: "Bench orders day-to-day hearing, asks trial court to decide within 6 months." },
      { court: "Supreme Court", title: "SC: Free legal aid is a right, not charity", detail: "Directs all states to display NALSA helpline 15100 prominently in every police station." },
      { court: "Bombay HC", title: "WhatsApp messages admitted as evidence in tenancy row", detail: "Court holds verified chat records admissible under the Evidence Act." },
      { court: "Madras HC", title: "Lok Adalat settles 12,000 pending cases in a single day", detail: "Motor accident and bank recovery matters saw the highest settlements." },
      { court: "Supreme Court", title: "SC launches AI-assisted translation of judgments", detail: "Key judgments to be available in Hindi, Kannada, Tamil and 6 more languages." },
      { court: "Allahabad HC", title: "Court warns against misuse of arrest in civil disputes", detail: "Police directed to record reasons in writing before every arrest." }
    ];

    const LINKS = [
      { name: "eCourts Services", url: "https://ecourts.gov.in", desc: "Check your case status, cause lists, court orders & hearing dates online.", descKn: "ನಿಮ್ಮ ಪ್ರಕರಣದ ಸ್ಥಿತಿ, ಕಾಸ್ ಪಟ್ಟಿ, ಆದೇಶಗಳು ಮತ್ತು ವಿಚಾರಣಾ ದಿನಾಂಕಗಳನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪರಿಶೀಲಿಸಿ.", icon: "Landmark" },
      { name: "Supreme Court of India", url: "https://www.sci.gov.in", desc: "Judgments, daily orders, causelists & e-filing at the apex court.", descKn: "ಸರ್ವೋಚ್ಚ ನ್ಯಾಯಾಲಯದ ತೀರ್ಪುಗಳು, ದೈನಂದಿನ ಆದೇಶಗಳು ಮತ್ತು ಇ-ಫೈಲಿಂಗ್.", icon: "Scale" },
      { name: "India Code", url: "https://www.indiacode.nic.in", desc: "Read every Indian Act and law — free, official & searchable.", descKn: "ಪ್ರತಿ ಭಾರತೀಯ ಕಾಯ್ದೆಯನ್ನು ಓದಿ — ಉಚಿತ, ಅಧಿಕೃತ ಮತ್ತು ಹುಡುಕಬಹುದಾದ.", icon: "BookOpen" },
      { name: "NALSA — Free Legal Aid", url: "https://nalsa.gov.in", desc: "Free legal aid for eligible citizens · Helpline 15100.", descKn: "ಅರ್ಹ ನಾಗರಿಕರಿಗೆ ಉಚಿತ ಕಾನೂನು ನೆರವು · ಸಹಾಯವಾಣಿ 15100.", icon: "HeartHandshake" }
    ];

    const UI = {
      "nav.explainer": { en: "Explainer", kn: "ವಿವರಣೆ" },
      "nav.categories": { en: "Categories", kn: "ವರ್ಗಗಳು" },
      "nav.live": { en: "Live Updates", kn: "ಲೈವ್ ಅಪ್ಡೇಟ್‌ಗಳು" },
      "nav.google": { en: "Google Search", kn: "ಗೂಗಲ್ ಹುಡುಕಾಟ" },
      "nav.links": { en: "Official Links", kn: "ಅಧಿಕೃತ ಲಿಂಕ್‌ಗಳು" },
      "hero.badge": { en: "Free legal literacy for every Indian", kn: "ಪ್ರತಿ ಭಾರತೀಯನಿಗೂ ಉಚಿತ ಕಾನೂನು ಜ್ಞಾನ" },
      "hero.titleA": { en: "My Lawyer Friend", kn: "ಮೈ ಲಾಯರ್ ಫ್ರೆಂಡ್" },
      "hero.titleB": { en: "Law Made Simple for Every Indian", kn: "ಪ್ರತಿ ಭಾರತೀಯನಿಗೂ ಸರಳ ಕಾನೂನು" },
      "hero.sub": { en: "Type any legal word — bail, FIR, divorce, cheque bounce — and get a plain-language explanation: what it means, the steps, how long it takes, and what it costs. No jargon. No fear.", kn: "ಯಾವುದೇ ಕಾನೂನು ಪದವನ್ನು ಟೈಪ್ ಮಾಡಿ — ಜಾಮೀನು, FIR, ವಿಚ್ಛೇದನ, ಚೆಕ್ ಬೌನ್ಸ್ — ಮತ್ತು ಸರಳ ಭಾಷೆಯಲ್ಲಿ ವಿವರಣೆ ಪಡೆಯಿರಿ." },
      "hero.placeholder": { en: "Try 'bail', 'FIR', 'divorce', 'cyber fraud'…", kn: "'ಜಾಮೀನು', 'FIR', 'ವಿಚ್ಛೇದನ' ಪ್ರಯತ್ನಿಸಿ…" },
      "hero.explain": { en: "Explain", kn: "ವಿವರಿಸಿ" },
      "hero.popular": { en: "Popular right now:", kn: "ಈಗ ಜನಪ್ರಿಯ:" },
      "hero.stat1": { en: "Legal terms explained", kn: "ವಿವರಿಸಿದ ಕಾನೂನು ಪದಗಳು" },
      "hero.stat2": { en: "Categories covered", kn: "ವರ್ಗಗಳು" },
      "hero.stat3": { en: "100% free forever", kn: "ಶಾಶ್ವತವಾಗಿ 100% ಉಚಿತ" },
      "explainer.kicker": { en: "AI Legal Explainer", kn: "AI ಕಾನೂನು ವಿವರಣೆ" },
      "explainer.title": { en: "Ask in plain words. Understand like a friend explained it.", kn: "ಸರಳ ಪದಗಳಲ್ಲಿ ಕೇಳಿ. ಸ್ನೇಹಿತ ವಿವರಿಸಿದಂತೆ ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ." },
      "explainer.meaning": { en: "What it means", kn: "ಇದರ ಅರ್ಥ" },
      "explainer.steps": { en: "Steps to follow", kn: "ಅನುಸರಿಸಬೇಕಾದ ಹಂತಗಳು" },
      "explainer.time": { en: "Time taken", kn: "ತೆಗೆದುಕೊಳ್ಳುವ ಸಮಯ" },
      "explainer.cost": { en: "Cost involved", kn: "ಒಳಗೊಂಡ ವೆಚ್ಚ" },
      "explainer.notfound": { en: "We don't have a simple explainer for that yet.", kn: "ಇದಕ್ಕೆ ಸರಳ ವಿವರಣೆ ಇನ್ನೂ ನಮ್ಮಲ್ಲಿಲ್ಲ." },
      "explainer.notfoundSub": { en: "Try one of the popular terms below — or search it on Google for official sources.", kn: "ಕೆಳಗಿನ ಜನಪ್ರಿಯ ಪದಗಳಲ್ಲಿ ಒಂದನ್ನು ಪ್ರಯತ್ನಿಸಿ — ಅಥವಾ ಅಧಿಕೃತ ಮೂಲಗಳಿಗಾಗಿ ಗೂಗಲ್‌ನಲ್ಲಿ ಹುಡುಕಿ." },
      "explainer.google": { en: "Search with Google", kn: "ಗೂಗಲ್‌ನಲ್ಲಿ ಹುಡುಕಿ" },
      "explainer.start": { en: "Search a legal term above, or pick a category below to begin.", kn: "ಮೇಲೆ ಕಾನೂನು ಪದವನ್ನು ಹುಡುಕಿ, ಅಥವಾ ಪ್ರಾರಂಭಿಸಲು ಕೆಳಗೆ ವರ್ಗವನ್ನು ಆಯ್ಕೆಮಾಡಿ." },
      "categories.kicker": { en: "Browse by category", kn: "ವರ್ಗದ ಪ್ರಕಾರ ಬ್ರೌಸ್ ಮಾಡಿ" },
      "categories.title": { en: "Everyday legal problems, organised for you", kn: "ದೈನಂದಿನ ಕಾನೂನು ಸಮಸ್ಯೆಗಳು, ನಿಮಗಾಗಿ ವ್ಯವಸ್ಥಿತ" },
      "categories.terms": { en: "explainer topics", kn: "ವಿವರಣಾ ವಿಷಯಗಳು" },
      "live.kicker": { en: "Live from the courts", kn: "ನ್ಯಾಯಾಲಯಗಳಿಂದ ಲೈವ್" },
      "live.title": { en: "Court updates, as they happen", kn: "ನ್ಯಾಯಾಲಯದ ಅಪ್ಡೇಟ್‌ಗಳು, ನಡೆದಂತೆ" },
      "live.note": { en: "Demo feed — sample headlines refresh automatically", kn: "ಡೆಮೊ ಫೀಡ್ — ಮಾದರಿ ಶೀರ್ಷಿಕೆಗಳು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ರಿಫ್ರೆಶ್ ಆಗುತ್ತವೆ" },
      "google.kicker": { en: "Deeper research", kn: "ಆಳವಾದ ಸಂಶೋಧನೆ" },
      "google.title": { en: "Take it further with Google", kn: "ಗೂಗಲ್‌ನೊಂದಿಗೆ ಮುಂದುವರಿಸಿ" },
      "google.sub": { en: "Need official judgments, forms or the latest news on your topic? Search Google directly — results open in a new tab.", kn: "ನಿಮ್ಮ ವಿಷಯದ ಅಧಿಕೃತ ತೀರ್ಪುಗಳು, ಫಾರ್ಮ್‌ಗಳು ಅಥವಾ ಇತ್ತೀಚಿನ ಸುದ್ದಿ ಬೇಕೇ? ನೇರವಾಗಿ ಗೂಗಲ್‌ನಲ್ಲಿ ಹುಡುಕಿ." },
      "google.placeholder": { en: "e.g. bail application format pdf…", kn: "ಉದಾ. ಜಾಮೀನು ಅರ್ಜಿ ನಮೂನೆ…" },
      "google.button": { en: "Search Google", kn: "ಗೂಗಲ್ ಹುಡುಕಿ" },
      "links.kicker": { en: "Trusted & official", kn: "ವಿಶ್ವಾಸಾರ್ಹ ಮತ್ತು ಅಧಿಕೃತ" },
      "links.title": { en: "Go straight to the source", kn: "ನೇರವಾಗಿ ಮೂಲಕ್ಕೆ ಹೋಗಿ" },
      "links.sub": { en: "Skip the middlemen. These are the official Government of India portals for cases, laws and free legal aid.", kn: "ಮಧ್ಯವರ್ತಿಗಳನ್ನು ಬಿಟ್ಟುಬಿಡಿ. ಪ್ರಕರಣಗಳು, ಕಾನೂನುಗಳು ಮತ್ತು ಉಚಿತ ಕಾನೂನು ನೆರವಿಗಾಗಿ ಇವು ಭಾರತ ಸರ್ಕಾರದ ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ಗಳು." },
      "links.visit": { en: "Visit site", kn: "ಸೈಟ್‌ಗೆ ಭೇಟಿ ನೀಡಿ" },
      "footer.disclaimer": { en: "For education only — not legal advice. Laws change; always consult a qualified lawyer for your specific situation.", kn: "ಶಿಕ್ಷಣಕ್ಕಾಗಿ ಮಾತ್ರ — ಕಾನೂನು ಸಲಹೆಯಲ್ಲ. ಕಾನೂನುಗಳು ಬದಲಾಗುತ್ತವೆ; ನಿಮ್ಮ ನಿರ್ದಿಷ್ಟ ಪರಿಸ್ಥಿತಿಗಾಗಿ ಯಾವಾಗಲೂ ಅರ್ಹ ವಕೀಲರನ್ನು ಸಂಪರ್ಕಿಸಿ." },
      "footer.tag": { en: "Built for every common Indian · My Lawyer Friend", kn: "ಪ್ರತಿ ಸಾಮಾನ್ಯ ಭಾರತೀಯನಿಗಾಗಿ · ಮೈ ಲಾಯರ್ ಫ್ರೆಂಡ್" }
    };

    // ============================================================
    //  ICONS (simple SVG strings)
    // ============================================================

    const ICONS = {
      ShieldAlert: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="M12 8v4"/><path d="M12 16h.01"/></svg>',
      FileText: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/></svg>',
      Users: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
      Home: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>',
      Cpu: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/></svg>',
      ShoppingBag: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>',
      Landmark: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" x2="21" y1="22" y2="22"/><line x1="6" x2="6" y1="18" y2="11"/><line x1="10" x2="10" y1="18" y2="11"/><line x1="14" x2="14" y1="18" y2="11"/><line x1="18" x2="18" y1="18" y2="11"/><polygon points="12 2 20 7 4 7"/></svg>',
      Scale: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/></svg>',
      BookOpen: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 7v14"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/></svg>',
      HeartHandshake: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/><path d="M12 5 9.04 7.96a2.17 2.17 0 0 0 0 3.08c.82.82 2.13.85 3 .07l2.07-1.9a2.82 2.82 0 0 1 3.79 0l2.96 2.66"/><path d="m18 15-2-2"/><path d="m15 18-2-2"/></svg>',
      Sparkles: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z"/><path d="M20 3v4"/><path d="M22 5h-4"/><path d="M4 17v2"/><path d="M5 18H3"/></svg>',
      TriangleAlert: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg>',
      Clock: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
      IndianRupee: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h12"/><path d="M6 8h12"/><path d="m6 13 8.5 8"/><path d="M6 13h3"/><path d="M9 13c6.667 0 6.667-10 0-10"/></svg>',
      Search: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>',
      Globe: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>',
      ArrowRight: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>',
      ChevronRight: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>',
      Languages: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/></svg>',
      ListChecks: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 17 2 2 4-4"/><path d="m3 7 2 2 4-4"/><path d="M13 6h8"/><path d="M13 12h8"/><path d="M13 18h8"/></svg>',
      BadgeCheck: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z"/><path d="m9 12 2 2 4-4"/></svg>',
      ExternalLink: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6"/><path d="M10 14 21 3"/><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/></svg>',
      Menu: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>',
      X: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>',
      Zap: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"/></svg>',
      Gavel: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m14.5 12.5-8 8a2.119 2.119 0 1 1-3-3l8-8"/><path d="m16 16 6-6"/><path d="m8 8 6-6"/><path d="m9 7 8 8"/><path d="m21 11-8-8"/></svg>'
    };

    // ============================================================
    //  HELPERS
    // ============================================================

    function t(key, lang) {
      return UI[key] ? UI[key][lang] : key;
    }

    function matchTerm(query) {
      const q = query.toLowerCase().trim();
      if (!q) return null;
      let best = null;
      for (const term of TERMS) {
        let score = 0;
        if (term.name.toLowerCase().includes(q) || q.includes(term.id.replace(/-/g, " "))) score += 6;
        for (const kw of term.keywords) {
          const k = kw.toLowerCase();
          if (k === q) score += 5;
          else if (k.includes(q) || q.includes(k)) score += 3;
        }
        if (score > 0 && (!best || score > best.score)) {
          best = { term, score };
        }
      }
      return best ? best.term : null;
    }

    function googleSearch(query) {
      const q = query.trim() ? `${query.trim()} legal help India` : "Indian law help";
      window.open(`https://www.google.com/search?q=${encodeURIComponent(q)}`, "_blank", "noopener,noreferrer");
    }

    function getCategoryLabel(catId, lang) {
      const cat = CATEGORIES.find(c => c.id === catId);
      return cat ? (lang === "kn" ? cat.labelKn : cat.label) : "";
    }

    // ============================================================
    //  RENDER APP
    // ============================================================

    const app = document.getElementById("app");

    // State
    let state = {
      lang: "en",
      query: "",
      selectedTerm: null,
      searched: false,
      activeCategory: null,
      mobileMenuOpen: false,
      googleQuery: "",
      tickerItems: NEWS.slice(0, 6),
      newsItems: NEWS.slice(0, 4).map((n, i) => ({ ...n, stamp: i === 0 ? "Just now" : `${(i + 1) * 7} min ago`, key: i })),
      newsKeyCounter: 4,
      activeNav: "top",
      logoPulse: false,
      explainerVisible: false
    };

    let newsInterval = null;
    let logoTimeout = null;

    // ---- Re-render ----
    function render() {
      const lang = state.lang;
      const selTerm = state.selectedTerm;
      const searched = state.searched;
      const cat = state.activeCategory;
      const filteredTerms = cat ? TERMS.filter(t => t.category === cat) : [];

      // Ticker
      const tickerHtml = state.tickerItems.concat(state.tickerItems).map((n, i) =>
        `<span class="ticker-item"><span style="color: var(--amber-300); font-weight: 600;">${n.court}:</span> ${n.title}</span>`
      ).join("");

      // Categories
      const catHtml = CATEGORIES.map(c => {
        const isActive = cat === c.id;
        const count = TERMS.filter(t => t.category === c.id).length;
        const iconSvg = ICONS[c.icon] || ICONS.FileText;
        return `
          <button class="category-btn ${isActive ? 'active' : ''}" data-cat="${c.id}">
            <span class="category-icon">${iconSvg}</span>
            <div class="font-display font-bold text-base sm:text-xl" style="color:#fff; margin-bottom:0.25rem;">${lang === "kn" ? c.labelKn : c.label}</div>
            <div style="font-size:0.6875rem; color: var(--slate-400); line-height:1.3;" class="sm:text-sm">${lang === "kn" ? c.taglineKn : c.tagline}</div>
            <div style="font-size:0.625rem; color: rgba(252,211,77,0.8); font-weight:600; margin-top:0.5rem;" class="sm:text-xs">${count} ${t("categories.terms", lang)}</div>
          </button>
        `;
      }).join("");

      // Filtered terms
      const filteredHtml = filteredTerms.length > 0 ? `
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-8 animate-fade-up">
          ${filteredTerms.map(term => `
            <button class="term-card" data-term-id="${term.id}">
              <div style="font-weight:600; color:#fff; font-size:0.875rem; margin-bottom:0.375rem;" class="sm:text-base">${lang === "kn" ? term.nameKn : term.name}</div>
              <p style="font-size:0.75rem; color: var(--slate-400); line-height:1.5;" class="sm:text-sm line-clamp-2">${lang === "kn" ? term.meaningKn : term.meaning}</p>
              <span style="display:inline-flex; align-items:center; gap:0.25rem; color: var(--amber-300); font-size:0.75rem; font-weight:700; margin-top:0.75rem;">
                ${t("hero.explain", lang)} ${ICONS.ArrowRight}
              </span>
            </button>
          `).join("")}
        </div>
      ` : "";

      // Explainer
      let explainerHtml = "";
      if (selTerm) {
        const term = selTerm;
        const timeVal = lang === "kn" ? term.timeKn : term.time;
        const costVal = lang === "kn" ? term.costKn : term.cost;
        explainerHtml = `
          <div class="explainer-panel ${state.explainerVisible ? 'visible' : 'hidden'}" id="explainer-panel">
            <div class="explainer-header">
              <div style="display:flex; align-items:center; gap:0.5rem; color: var(--amber-300); font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.18em; margin-bottom:0.5rem;">
                ${ICONS.Sparkles} ${getCategoryLabel(term.category, lang)}
              </div>
              <h3 class="font-display font-bold text-2xl sm:text-4xl" style="color:#fff;">${lang === "kn" ? term.nameKn : term.name}</h3>
            </div>
            <div style="padding:1.5rem 1.5rem;" class="sm:p-10">
              <div style="margin-bottom:1.75rem;">
                <div style="display:flex; align-items:center; gap:0.5rem; color:#fde68a; font-weight:700; font-size:0.875rem; text-transform:uppercase; letter-spacing:0.05em; margin-bottom:0.75rem;">
                  ${ICONS.BookOpen} ${t("explainer.meaning", lang)}
                </div>
                <p style="color: rgba(226,232,240,0.95); font-size:0.875rem; line-height:1.7;" class="sm:text-base">${lang === "kn" ? term.meaningKn : term.meaning}</p>
              </div>
              <div style="margin-bottom:1.75rem;">
                <div style="display:flex; align-items:center; gap:0.5rem; color:#fde68a; font-weight:700; font-size:0.875rem; text-transform:uppercase; letter-spacing:0.05em; margin-bottom:1rem;">
                  ${ICONS.ListChecks} ${t("explainer.steps", lang)}
                </div>
                <ol style="display:flex; flex-direction:column; gap:0.75rem; list-style:none; padding:0; margin:0;">
                  ${term.steps.map((step, i) => `
                    <li style="display:flex; gap:0.875rem; align-items:flex-start;">
                      <span class="step-number">${i + 1}</span>
                      <span style="color: var(--slate-300); font-size:0.875rem; line-height:1.7; padding-top:0.25rem;" class="sm:text-[15px]">${step}</span>
                    </li>
                  `).join("")}
                </ol>
              </div>
              <div style="display:grid; gap:0.75rem; margin-bottom:1.75rem;" class="sm:grid-cols-2">
                <div class="info-box">
                  <div style="display:flex; align-items:center; gap:0.5rem; color: var(--amber-300); font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.05em; margin-bottom:0.5rem;">
                    ${ICONS.Clock} ${t("explainer.time", lang)}
                  </div>
                  <div style="color:#fff; font-size:0.875rem; font-weight:500; line-height:1.6;" class="sm:text-[15px]">${timeVal}</div>
                </div>
                <div class="info-box">
                  <div style="display:flex; align-items:center; gap:0.5rem; color: var(--amber-300); font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.05em; margin-bottom:0.5rem;">
                    ${ICONS.IndianRupee} ${t("explainer.cost", lang)}
                  </div>
                  <div style="color:#fff; font-size:0.875rem; font-weight:500; line-height:1.6;" class="sm:text-[15px]">${costVal}</div>
                </div>
              </div>
              <button class="btn-glass" data-google-term="${term.name}">
                ${ICONS.Globe} ${t("explainer.google", lang)} ${ICONS.ChevronRight}
              </button>
            </div>
          </div>
        `;
      } else if (searched) {
        explainerHtml = `
          <div class="glass rounded-3xl p-8 sm:p-12 text-center max-w-2xl mx-auto animate-fade-up">
            <div style="width:3.5rem; height:3.5rem; border-radius:1rem; background: rgba(251,191,36,0.1); border:1px solid rgba(251,191,36,0.3); display:flex; align-items:center; justify-content:center; margin:0 auto 1.25rem;">
              ${ICONS.TriangleAlert}
            </div>
            <h3 class="font-display font-bold text-2xl" style="color:#fff; margin-bottom:0.5rem;">${t("explainer.notfound", lang)}</h3>
            <p style="color: var(--slate-400); font-size:0.875rem; margin-bottom:1.5rem;" class="sm:text-base">${t("explainer.notfoundSub", lang)}</p>
            <div style="display:flex; flex-wrap:wrap; justify-content:center; gap:0.5rem; margin-bottom:1.75rem;">
              ${["bail","FIR","divorce","cheque bounce","cyber fraud","consumer complaint"].map(q => `
                <button class="popular-term-btn" data-term="${q}" style="padding:0.375rem 0.875rem; border-radius:9999px; border:1px solid rgba(251,191,36,0.25); color: var(--amber-200); font-size:0.875rem; background:transparent; cursor:pointer; transition:all 0.2s;">
                  ${q}
                </button>
              `).join("")}
            </div>
            <button class="btn-gold" data-google-query="${state.query}">
              ${ICONS.Globe} ${t("explainer.google", lang)}
            </button>
          </div>
        `;
      } else {
        explainerHtml = `
          <div class="glass rounded-3xl p-8 sm:p-10 text-center max-w-2xl mx-auto">
            <div style="color: rgba(252,211,77,0.7); margin:0 auto 1rem;">${ICONS.Scale}</div>
            <p style="color: var(--slate-300); font-size:0.875rem; line-height:1.7;" class="sm:text-base">${t("explainer.start", lang)}</p>
          </div>
        `;
      }

      // News items
      const newsHtml = state.newsItems.map((n, i) => `
        <article class="news-card" data-news-key="${n.key}">
          ${i === 0 ? `
            <span style="position:absolute; top:1rem; right:1rem; display:flex; align-items:center; gap:0.375rem; padding:0.25rem 0.625rem; border-radius:9999px; background: rgba(239,68,68,0.15); border:1px solid rgba(239,68,68,0.4); color:#f87171; font-size:0.625rem; font-weight:700; text-transform:uppercase; letter-spacing:0.05em;">
              <span style="width:0.375rem; height:0.375rem; border-radius:9999px; background:#ef4444; display:inline-block;" class="live-dot"></span> Live
            </span>
          ` : ""}
          <div style="display:flex; align-items:center; gap:0.5rem; color: rgba(252,211,77,0.9); font-size:0.6875rem; font-weight:700; text-transform:uppercase; letter-spacing:0.16em; margin-bottom:0.625rem;">
            ${ICONS.Zap} ${n.court}
          </div>
          <h3 style="font-weight:600; color:#fff; font-size:0.875rem; line-height:1.4; margin-bottom:0.5rem; padding-right:3.5rem;" class="sm:text-base">${n.title}</h3>
          <p style="color: var(--slate-400); font-size:0.75rem; line-height:1.6; margin-bottom:0.75rem;" class="sm:text-sm">${n.detail}</p>
          <div style="font-size:0.6875rem; color: var(--slate-500); display:flex; align-items:center; gap:0.375rem;">
            ${ICONS.Clock} ${n.stamp}
          </div>
        </article>
      `).join("");

      // Links
      const linksHtml = LINKS.map(l => `
        <a href="${l.url}" target="_blank" rel="noopener noreferrer" class="link-card">
          <span class="link-icon">${ICONS[l.icon] || ICONS.Landmark}</span>
          <div class="font-display font-bold text-lg" style="color:#fff; margin-bottom:0.5rem;">${l.name}</div>
          <p style="font-size:0.75rem; color: var(--slate-400); line-height:1.6; flex:1;" class="sm:text-sm">${lang === "kn" ? l.descKn : l.desc}</p>
          <span style="display:inline-flex; align-items:center; gap:0.375rem; color: var(--amber-300); font-size:0.875rem; font-weight:700; margin-top:1.25rem;">
            ${t("links.visit", lang)} ${ICONS.ExternalLink}
          </span>
        </a>
      `).join("");

      // Full render
      app.innerHTML = `
        <!-- Ticker -->
        <div style="background: linear-gradient(to right, #0d1730, #131f42, #0d1730); border-bottom:1px solid rgba(251,191,36,0.15); overflow:hidden;">
          <div style="display:flex; align-items:center;">
            <div class="live-badge">
              <span style="width:0.5rem; height:0.5rem; border-radius:9999px; background: var(--navy-800); display:inline-block;" class="live-dot"></span> Live
            </div>
            <div class="ticker-wrap">
              <div class="ticker-track" style="display:flex; white-space:nowrap; padding:0.5rem 0;">
                ${tickerHtml}
              </div>
            </div>
          </div>
        </div>

        <!-- Header -->
        <header style="position:sticky; top:0; z-index:40; border-bottom:1px solid rgba(255,255,255,0.05); background: rgba(7,13,31,0.8); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);">
          <div class="container" style="display:flex; align-items:center; justify-content:space-between; height:4rem;" class="sm:height:4.5rem">
            <button id="logo-btn" style="display:flex; align-items:center; gap:0.75rem; text-align:left; border-radius:0.75rem; padding:0.25rem 0.5rem; margin-left:-0.5rem; background:transparent; border:none; cursor:pointer; transition:all 0.3s; ${state.logoPulse ? 'background: rgba(251,191,36,0.25); box-shadow: 0 0 0 2px rgba(251,191,36,0.7); transform: scale(1.04);' : state.activeNav === 'top' ? 'background: rgba(251,191,36,0.1); box-shadow: 0 0 0 1px rgba(251,191,36,0.3);' : ''}">
              <span style="width:2.5rem; height:2.5rem; border-radius:0.75rem; background: linear-gradient(to bottom right, var(--amber-300), var(--amber-600)); display:flex; align-items:center; justify-content:center; box-shadow: 0 10px 15px -3px rgba(245,158,11,0.25);">
                ${ICONS.Scale}
              </span>
              <span>
                <span style="display:block; font-family:Fraunces,serif; font-weight:700; font-size:1.125rem; line-height:1; background: linear-gradient(120deg, #f6e27a, #d4af37 35%, #f9eec3 55%, #c9962e 80%, #f6e27a); -webkit-background-clip:text; background-clip:text; color:transparent;">My Lawyer Friend</span>
                <span style="display:block; font-size:0.625rem; letter-spacing:0.22em; text-transform:uppercase; color: var(--slate-400); margin-top:0.25rem;">Court Case Explainer</span>
              </span>
            </button>
            <nav class="hidden lg:flex" style="align-items:center; gap:1.75rem; font-size:0.875rem; font-weight:500; color: var(--slate-300);">
              ${["explainer","categories","live","google","links"].map(key => `
                <button class="nav-btn" data-nav="${key}" style="padding:0.375rem 0.75rem; border-radius:9999px; background:transparent; border:none; cursor:pointer; transition:all 0.2s; color:inherit; font:inherit; ${state.activeNav === key ? 'color: var(--amber-300); background: rgba(251,191,36,0.1); box-shadow: 0 0 0 1px rgba(251,191,36,0.3);' : ''}">${t(`nav.${key}`, lang)}</button>
              `).join("")}
            </nav>
            <div style="display:flex; align-items:center; gap:0.5rem;">
              <button id="lang-toggle" class="lang-toggle">
                ${ICONS.Languages} ${lang === "en" ? "ಕನ್ನಡ" : "English"}
              </button>
              <button id="mobile-menu-btn" class="lg:hidden" style="padding:0.5rem; border-radius:0.5rem; background: linear-gradient(145deg, rgba(255,255,255,0.07), rgba(255,255,255,0.025)); border:1px solid rgba(212,175,55,0.16); color: var(--slate-200); cursor:pointer;">
                ${state.mobileMenuOpen ? ICONS.X : ICONS.Menu}
              </button>
            </div>
          </div>
          ${state.mobileMenuOpen ? `
            <nav style="border-top:1px solid rgba(255,255,255,0.05); background: rgba(10,17,40,0.95); backdrop-filter: blur(24px); padding:0.75rem 1rem; display:flex; flex-direction:column; gap:0.25rem; font-size:0.875rem;">
              ${["explainer","categories","live","google","links"].map(key => `
                <button class="nav-btn-mobile" data-nav="${key}" style="text-align:left; padding:0.625rem 0.75rem; border-radius:0.5rem; background:transparent; border:none; cursor:pointer; transition:all 0.2s; color: var(--slate-200); font:inherit; ${state.activeNav === key ? 'background: rgba(251,191,36,0.1); color: var(--amber-300); box-shadow: 0 0 0 1px rgba(251,191,36,0.3);' : ''}">${t(`nav.${key}`, lang)}</button>
              `).join("")}
            </nav>
          ` : ""}
        </header>

        <!-- Hero -->
        <section style="position:relative; overflow:hidden;">
          <div class="bg-grid-gold" style="position:absolute; inset:0;"></div>
          <div style="position:absolute; top:-8rem; left:50%; transform:translateX(-50%); width:720px; height:420px; background: rgba(245,158,11,0.15); filter:blur(130px); border-radius:9999px; pointer-events:none;"></div>
          <div style="position:absolute; top:10rem; left:-6rem; width:18rem; height:18rem; background: rgba(79,70,229,0.2); filter:blur(110px); border-radius:9999px; pointer-events:none;" class="animate-floaty"></div>
          <div style="position:absolute; top:16rem; right:-6rem; width:18rem; height:18rem; background: rgba(251,191,36,0.1); filter:blur(110px); border-radius:9999px; pointer-events:none;" class="animate-floaty"></div>
          <div class="container" style="position:relative; max-width:64rem; padding-top:3.5rem; padding-bottom:3.5rem; text-align:center;" class="sm:pt-24 sm:pb-20">
            <div class="animate-fade-up" style="display:inline-flex; align-items:center; gap:0.5rem; padding:0.375rem 1rem; border-radius:9999px; background: linear-gradient(145deg, rgba(255,255,255,0.07), rgba(255,255,255,0.025)); border:1px solid rgba(212,175,55,0.16); font-size:0.75rem; color: #fde68a; font-weight:500; margin-bottom:1.5rem;" class="sm:text-sm">
              ${ICONS.Sparkles} ${t("hero.badge", lang)}
            </div>
            <h1 class="animate-fade-up-1 font-display font-bold" style="font-size:2.25rem; line-height:1.05; letter-spacing:-0.025em;" class="sm:text-6xl lg:text-7xl">
              <span class="text-gold-gradient">${t("hero.titleA", lang)}</span><br>
              <span style="color:#fff;">${t("hero.titleB", lang)}</span>
            </h1>
            <p class="animate-fade-up-2" style="margin-top:1.25rem; color: rgba(203,213,225,0.9); font-size:0.875rem; max-width:42rem; margin-left:auto; margin-right:auto; line-height:1.7;" class="sm:mt-6 sm:text-lg">${t("hero.sub", lang)}</p>
            <form id="hero-form" class="animate-fade-up-3" style="margin-top:2rem; max-width:42rem; margin-left:auto; margin-right:auto;" class="sm:mt-10">
              <div class="glass gold-ring" style="border-radius:1rem; padding:0.5rem; display:flex; flex-direction:column; gap:0.5rem; transition:all 0.2s;" class="sm:flex-row sm:rounded-full">
                <div style="display:flex; align-items:center; flex:1; min-width:0; gap:0.5rem; padding:0 0.75rem;">
                  ${ICONS.Search}
                  <input id="hero-input" type="text" value="${state.query}" placeholder="${t("hero.placeholder", lang)}" style="width:100%; min-width:0; background:transparent; border:none; outline:none; font-size:0.875rem; color:#fff; padding:0.625rem 0;" class="sm:text-base hero-input" aria-label="Search legal term">
                </div>
                <div style="display:flex; gap:0.5rem;">
                  <button type="submit" class="btn-gold" style="flex:1; padding:0.625rem 1.5rem; border-radius:0.75rem;" class="sm:flex-none sm:rounded-full">${t("hero.explain", lang)}</button>
                  <button type="button" id="hero-google-btn" class="btn-glass" style="padding:0.625rem 1rem; border-radius:0.75rem;" class="sm:rounded-full">
                    ${ICONS.Globe} <span class="hidden sm:inline">Google</span>
                  </button>
                </div>
              </div>
            </form>
            <div class="animate-fade-up-3" style="margin-top:1.25rem; display:flex; flex-wrap:wrap; align-items:center; justify-content:center; gap:0.5rem; font-size:0.75rem;" class="sm:text-sm">
              <span style="color: var(--slate-400);">${t("hero.popular", lang)}</span>
              ${["bail","FIR","divorce","cheque bounce","cyber fraud","consumer complaint"].map(q => `
                <button class="popular-term-btn" data-term="${q}" style="padding:0.375rem 0.75rem; border-radius:9999px; border:1px solid rgba(251,191,36,0.25); color: rgba(253,230,138,0.9); background:transparent; cursor:pointer; transition:all 0.2s;">${q}</button>
              `).join("")}
            </div>
            <div style="margin-top:2.5rem; display:grid; grid-template-columns:repeat(3,1fr); gap:0.75rem; max-width:36rem; margin-left:auto; margin-right:auto;" class="sm:mt-14">
              ${[
                [String(TERMS.length), t("hero.stat1", lang)],
                [String(CATEGORIES.length), t("hero.stat2", lang)],
                ["₹0", t("hero.stat3", lang)]
              ].map(([val, lab]) => `
                <div class="stat-card">
                  <div class="font-display font-bold text-2xl sm:text-3xl text-gold-gradient">${val}</div>
                  <div style="font-size:0.625rem; color: var(--slate-400); margin-top:0.25rem; line-height:1.3;" class="sm:text-xs">${lab}</div>
                </div>
              `).join("")}
            </div>
          </div>
          <div style="position:relative; height:1px; background: linear-gradient(to right, transparent, rgba(251,191,36,0.4), transparent);"></div>
        </section>

        <!-- Explainer -->
        <section id="explainer" style="position:relative; max-width:64rem; margin:0 auto; padding:3.5rem 1.25rem;" class="sm:py-20 container">
          <div style="text-align:center; margin-bottom:2rem;" class="sm:mb-12">
            <div style="display:inline-flex; align-items:center; gap:0.5rem; color: var(--amber-300); font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.2em; margin-bottom:0.75rem;">
              ${ICONS.Gavel} ${t("explainer.kicker", lang)}
            </div>
            <h2 class="font-display font-bold text-3xl sm:text-5xl" style="color:#fff; line-height:1.2;">${t("explainer.title", lang)}</h2>
          </div>
          ${explainerHtml}
        </section>

        <!-- Categories -->
        <section id="categories" style="position:relative; border-top:1px solid rgba(255,255,255,0.05); border-bottom:1px solid rgba(255,255,255,0.05); background: rgba(10,19,48,0.6);">
          <div class="container" style="max-width:80rem; padding-top:3.5rem; padding-bottom:3.5rem;" class="sm:py-20">
            <div style="text-align:center; margin-bottom:2.5rem;">
              <div style="color: var(--amber-300); font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.2em; margin-bottom:0.75rem;">${t("categories.kicker", lang)}</div>
              <h2 class="font-display font-bold text-3xl sm:text-5xl" style="color:#fff;">${t("categories.title", lang)}</h2>
            </div>
            <div style="display:grid; gap:0.75rem;" class="grid-cols-2 lg:grid-cols-3 sm:gap-5">
              ${catHtml}
            </div>
            ${filteredHtml}
          </div>
        </section>

        <!-- Live -->
        <section id="live" class="container" style="max-width:80rem; padding:3.5rem 1.25rem;" class="sm:py-20">
          <div style="display:flex; flex-direction:column; gap:0.75rem; margin-bottom:2rem;" class="sm:flex-row sm:items-end sm:justify-between sm:mb-10">
            <div>
              <div style="display:flex; align-items:center; gap:0.5rem; color: var(--amber-300); font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.2em; margin-bottom:0.75rem;">
                <span style="width:0.625rem; height:0.625rem; border-radius:9999px; background:#ef4444; display:inline-block;" class="live-dot"></span>
                ${t("live.kicker", lang)}
              </div>
              <h2 class="font-display font-bold text-3xl sm:text-5xl" style="color:#fff;">${t("live.title", lang)}</h2>
            </div>
            <p style="font-size:0.75rem; color: var(--slate-500); font-style:italic;">${t("live.note", lang)}</p>
          </div>
          <div id="news-grid" style="display:grid; gap:1rem;" class="sm:grid-cols-2">
            ${newsHtml}
          </div>
        </section>

        <!-- Google -->
        <section id="google" style="position:relative; border-top:1px solid rgba(255,255,255,0.05); border-bottom:1px solid rgba(255,255,255,0.05); background: rgba(10,19,48,0.6); overflow:hidden;">
          <div style="position:absolute; top:0; right:0; width:24rem; height:24rem; background: rgba(245,158,11,0.1); filter:blur(120px); border-radius:9999px; pointer-events:none;"></div>
          <div class="container" style="position:relative; max-width:48rem; padding-top:3.5rem; padding-bottom:3.5rem; text-align:center;" class="sm:py-20">
            <div style="color: var(--amber-300); font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.2em; margin-bottom:0.75rem;">${t("google.kicker", lang)}</div>
            <h2 class="font-display font-bold text-3xl sm:text-5xl" style="color:#fff; margin-bottom:1rem;">${t("google.title", lang)}</h2>
            <p style="color: var(--slate-400); font-size:0.875rem; margin-bottom:2rem; max-width:36rem; margin-left:auto; margin-right:auto; line-height:1.7;" class="sm:text-base">${t("google.sub", lang)}</p>
            <form id="google-form" class="glass gold-ring google-bar" style="max-width:36rem; margin:0 auto; border-radius:1rem; padding:0.5rem; transition:all 0.2s;">
              <div style="display:flex; align-items:center; flex:1; gap:0.75rem; padding:0 1rem;">
                <span class="font-display font-bold text-lg" style="color:#fff; user-select:none;">G</span>
                <input id="google-input" type="text" value="${state.googleQuery}" placeholder="${t("google.placeholder", lang)}" style="width:100%; background:transparent; border:none; outline:none; font-size:0.875rem; color:#fff; padding:0.75rem 0;" class="sm:text-base hero-input" aria-label="Google search">
              </div>
              <button type="submit" class="btn-gold" style="padding:0.75rem 1.75rem; border-radius:0.75rem; display:flex; align-items:center; justify-content:center; gap:0.5rem;">
                ${ICONS.Search} ${t("google.button", lang)}
              </button>
            </form>
            <p style="font-size:0.6875rem; color: var(--slate-500); margin-top:1rem;">Opens google.com in a new tab · Free forever</p>
          </div>
        </section>

        <!-- Links -->
        <section id="links" class="container" style="max-width:80rem; padding:3.5rem 1.25rem;" class="sm:py-20">
          <div style="text-align:center; margin-bottom:2.5rem;">
            <div style="color: var(--amber-300); font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.2em; margin-bottom:0.75rem;">${t("links.kicker", lang)}</div>
            <h2 class="font-display font-bold text-3xl sm:text-5xl" style="color:#fff; margin-bottom:1rem;">${t("links.title", lang)}</h2>
            <p style="color: var(--slate-400); font-size:0.875rem; max-width:42rem; margin:0 auto; line-height:1.7;" class="sm:text-base">${t("links.sub", lang)}</p>
          </div>
          <div style="display:grid; gap:1rem;" class="sm:grid-cols-2 lg:grid-cols-4 sm:gap-5">
            ${linksHtml}
          </div>
        </section>

        <!-- Footer -->
        <footer style="border-top:1px solid rgba(251,191,36,0.15); background:#050a1a;">
          <div class="container" style="max-width:80rem; padding-top:2.5rem; padding-bottom:2.5rem;" class="sm:py-14">
            <div style="display:flex; flex-direction:column; align-items:center; justify-content:space-between; gap:1.5rem; margin-bottom:2rem;" class="sm:flex-row">
              <div style="display:flex; align-items:center; gap:0.75rem;">
                <span style="width:2.5rem; height:2.5rem; border-radius:0.75rem; background: linear-gradient(to bottom right, var(--amber-300), var(--amber-600)); display:flex; align-items:center; justify-content:center;">
                  ${ICONS.Scale}
                </span>
                <div>
                  <div class="font-display font-bold text-lg text-gold-gradient">My Lawyer Friend</div>
                  <div style="font-size:0.625rem; letter-spacing:0.22em; text-transform:uppercase; color: var(--slate-500);">Your Friend in Law · Bridge to Justice</div>
                </div>
              </div>
              <div style="display:flex; align-items:center; gap:0.5rem; font-size:0.75rem; color: var(--slate-500);">
                ${ICONS.BadgeCheck} ${t("footer.tag", lang)}
              </div>
            </div>
            <div style="border-radius:1rem; border:1px solid rgba(251,191,36,0.2); background: rgba(251,191,36,0.05); padding:1rem 1.25rem; display:flex; gap:0.75rem;">
              ${ICONS.TriangleAlert}
              <p style="font-size:0.75rem; color: rgba(253,230,138,0.8); line-height:1.7;" class="sm:text-sm">
                <span style="font-weight:700; color:#fde68a;">Disclaimer: </span>${t("footer.disclaimer", lang)}
              </p>
            </div>
            <div style="text-align:center; font-size:0.6875rem; color: var(--slate-600); margin-top:2rem;">
              © ${new Date().getFullYear()} My Lawyer Friend · A student portfolio project for legal literacy
            </div>
          </div>
        </footer>
      `;

      // ---- Attach event listeners ----
      // Hero form
      const heroForm = document.getElementById("hero-form");
      if (heroForm) {
        heroForm.addEventListener("submit", (e) => {
          e.preventDefault();
          const input = document.getElementById("hero-input");
          if (input) {
            state.query = input.value;
            explainQuery(state.query);
          }
        });
      }

      // Hero google
      const heroGoogle = document.getElementById("hero-google-btn");
      if (heroGoogle) {
        heroGoogle.addEventListener("click", () => {
          const input = document.getElementById("hero-input");
          const q = input ? input.value : state.query;
          googleSearch(q);
        });
      }

      // Hero input live binding
      const heroInput = document.getElementById("hero-input");
      if (heroInput) {
        heroInput.addEventListener("input", (e) => {
          state.query = e.target.value;
        });
      }

      // Popular term buttons
      document.querySelectorAll(".popular-term-btn").forEach(btn => {
        btn.addEventListener("click", () => {
          const term = btn.dataset.term;
          if (term) {
            state.query = term;
            explainQuery(term);
          }
        });
      });

      // Google search buttons (in explainer)
      document.querySelectorAll("[data-google-term]").forEach(btn => {
        btn.addEventListener("click", () => {
          googleSearch(btn.dataset.googleTerm);
        });
      });
      document.querySelectorAll("[data-google-query]").forEach(btn => {
        btn.addEventListener("click", () => {
          googleSearch(btn.dataset.googleQuery || state.query);
        });
      });

      // Category buttons
      document.querySelectorAll(".category-btn").forEach(btn => {
        btn.addEventListener("click", () => {
          const catId = btn.dataset.cat;
          state.activeCategory = state.activeCategory === catId ? null : catId;
          render();
        });
      });

      // Term cards
      document.querySelectorAll(".term-card").forEach(card => {
        card.addEventListener("click", () => {
          const termId = card.dataset.termId;
          const term = TERMS.find(t => t.id === termId);
          if (term) {
            state.selectedTerm = term;
            state.searched = true;
            state.query = term.name;
            state.explainerVisible = true;
            render();
            document.getElementById("explainer")?.scrollIntoView({ behavior: "smooth", block: "start" });
          }
        });
      });

      // Nav buttons (desktop)
      document.querySelectorAll(".nav-btn").forEach(btn => {
        btn.addEventListener("click", () => {
          navigateTo(btn.dataset.nav);
        });
      });

      // Nav buttons (mobile)
      document.querySelectorAll(".nav-btn-mobile").forEach(btn => {
        btn.addEventListener("click", () => {
          state.mobileMenuOpen = false;
          navigateTo(btn.dataset.nav);
        });
      });

      // Logo button
      const logoBtn = document.getElementById("logo-btn");
      if (logoBtn) {
        logoBtn.addEventListener("click", () => {
          navigateTo("top");
          state.logoPulse = true;
          if (logoTimeout) clearTimeout(logoTimeout);
          logoTimeout = setTimeout(() => { state.logoPulse = false; render(); }, 700);
          render();
        });
      }

      // Language toggle
      const langToggle = document.getElementById("lang-toggle");
      if (langToggle) {
        langToggle.addEventListener("click", () => {
          state.lang = state.lang === "en" ? "kn" : "en";
          render();
        });
      }

      // Mobile menu toggle
      const mobileBtn = document.getElementById("mobile-menu-btn");
      if (mobileBtn) {
        mobileBtn.addEventListener("click", () => {
          state.mobileMenuOpen = !state.mobileMenuOpen;
          render();
        });
      }

      // Google form
      const googleForm = document.getElementById("google-form");
      if (googleForm) {
        googleForm.addEventListener("submit", (e) => {
          e.preventDefault();
          const input = document.getElementById("google-input");
          if (input) {
            state.googleQuery = input.value;
            googleSearch(state.googleQuery);
          }
        });
      }
      const googleInput = document.getElementById("google-input");
      if (googleInput) {
        googleInput.addEventListener("input", (e) => {
          state.googleQuery = e.target.value;
        });
      }

      // Explainer panel visibility
      const panel = document.getElementById("explainer-panel");
      if (panel) {
        requestAnimationFrame(() => {
          panel.classList.remove("hidden");
          panel.classList.add("visible");
        });
      }
    }

    // ---- Explain query ----
    function explainQuery(q) {
      const term = matchTerm(q);
      state.selectedTerm = term;
      state.searched = true;
      state.explainerVisible = true;
      render();
      document.getElementById("explainer")?.scrollIntoView({ behavior: "smooth", block: "start" });
    }

    // ---- Navigate ----
    function navigateTo(section) {
      state.activeNav = section;
      if (section === "top") {
        window.scrollTo({ top: 0, behavior: "smooth" });
      } else {
        const el = document.getElementById(section);
        if (el) {
          el.scrollIntoView({ behavior: "smooth", block: "start" });
        }
      }
      render();
    }

    // ---- News ticker ----
    function startNewsTicker() {
      if (newsInterval) clearInterval(newsInterval);
      newsInterval = setInterval(() => {
        const nextIdx = state.newsKeyCounter % NEWS.length;
        const newItem = NEWS[nextIdx];
        state.newsKeyCounter += 1;
        state.newsItems = [
          { ...newItem, stamp: "Just now", key: state.newsKeyCounter },
          ...state.newsItems.slice(0, 3)
        ];
        render();
      }, 9000);
    }

    // ---- Initial render ----
    render();
    startNewsTicker();
  </script>
</body>
</html>
