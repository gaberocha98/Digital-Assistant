const fs = require('fs');
const path = require('path');
const INTER = fs.readFileSync(path.join(__dirname, 'fonts', 'inter-embed.css'), 'utf8');

const TOTAL = 7;

function dots(active) {
  let d = '';
  for (let i = 0; i < TOTAL; i++) {
    d += `<span class="dot ${i === active ? 'on' : ''}"></span>`;
  }
  return d;
}

function chrome(idx) {
  const num = String(idx + 1).padStart(2, '0');
  return {
    top: `
      <div class="topbar">
        <div class="brand">
          <div class="mark">E</div>
          <div class="wordmark">EON<span>RESEARCH</span></div>
        </div>
        <div class="counter">${num}<span>/07</span></div>
      </div>`,
    bottom: `
      <div class="botbar">
        <div class="url">eonresearch.bio</div>
        <div class="dots">${dots(idx)}</div>
      </div>`,
  };
}

function slideInner(s, idx) {
  if (s.type === 'cover') {
    return `
      <div class="content cover">
        <div class="eyebrow">${s.eyebrow}</div>
        <h1 class="cover-title">${s.title}</h1>
        <div class="rule"></div>
        <p class="cover-sub">${s.sub}</p>
        <div class="swipe">Swipe <span>&rarr;</span></div>
      </div>`;
  }
  if (s.type === 'list') {
    const items = s.items.map(
      (t, i) => `<li><span class="num">${String(i + 1).padStart(2, '0')}</span><span class="li-txt">${t}</span></li>`
    ).join('');
    return `
      <div class="content">
        <div class="eyebrow">${s.eyebrow}</div>
        <h2 class="body-title">${s.title}</h2>
        <ul class="list">${items}</ul>
      </div>`;
  }
  if (s.type === 'cta') {
    return `
      <div class="content cta">
        <div class="eyebrow">${s.eyebrow}</div>
        <h2 class="cta-title">${s.title}</h2>
        <p class="body-text">${s.body}</p>
        <div class="cta-btn">${s.button}<span class="arr">&rarr;</span></div>
      </div>`;
  }
  // body
  return `
    <div class="content">
      <div class="eyebrow">${s.eyebrow}</div>
      ${s.title ? `<h2 class="body-title">${s.title}</h2>` : ''}
      <p class="body-text">${s.body}</p>
      ${s.cite ? `<div class="cite">${s.cite}</div>` : ''}
    </div>`;
}

function renderSlide(s, idx) {
  const c = chrome(idx);
  return `<!doctype html><html><head><meta charset="utf-8"><style>
  ${INTER}
  *{margin:0;padding:0;box-sizing:border-box;}
  :root{
    --teal:#0D9488; --teal-d:#115E59; --mint:#CCFBF1;
    --amber:#F59E0B; --amber-s:#FEF3C7;
    --ink:#E8EEF0; --dim:#7C8B92;
  }
  html,body{width:1080px;height:1350px;}
  body{
    font-family:'Inter',sans-serif;
    background:
      radial-gradient(1200px 700px at 78% -10%, rgba(13,148,136,0.20), transparent 60%),
      radial-gradient(900px 600px at 10% 110%, rgba(17,94,89,0.18), transparent 55%),
      linear-gradient(160deg,#0a1615 0%, #071110 55%, #050d0c 100%);
    color:var(--ink);
    -webkit-font-smoothing:antialiased;
    overflow:hidden;
  }
  .frame{
    position:relative; width:1080px; height:1350px;
    padding:74px 84px;
    display:flex; flex-direction:column;
  }
  .frame::after{ /* subtle inner border */
    content:''; position:absolute; inset:26px; border:1px solid rgba(204,251,241,0.07);
    border-radius:28px; pointer-events:none;
  }

  /* top bar */
  .topbar{display:flex; align-items:center; justify-content:space-between;}
  .brand{display:flex; align-items:center; gap:18px;}
  .mark{
    width:66px;height:66px;border-radius:18px;
    background:linear-gradient(150deg,var(--teal),var(--teal-d));
    display:flex;align-items:center;justify-content:center;
    font-weight:900;font-size:38px;color:#fff;
    box-shadow:0 8px 30px rgba(13,148,136,0.35);
    border:1px solid rgba(204,251,241,0.25);
  }
  .wordmark{font-weight:800;font-size:27px;letter-spacing:1px;line-height:1;color:#fff;}
  .wordmark span{display:block;font-weight:600;font-size:15px;letter-spacing:6px;color:var(--teal);margin-top:5px;}
  .counter{font-weight:800;font-size:30px;color:var(--amber);letter-spacing:1px;}
  .counter span{color:var(--dim);font-weight:600;font-size:24px;}

  /* content */
  .content{flex:1;display:flex;flex-direction:column;justify-content:center;padding:0 6px;}
  .eyebrow{
    font-weight:700;font-size:24px;letter-spacing:6px;color:var(--teal);
    text-transform:uppercase;margin-bottom:34px;display:flex;align-items:center;gap:16px;
  }
  .eyebrow::before{content:'';width:44px;height:3px;background:var(--amber);border-radius:2px;}

  .hl{color:var(--amber);font-weight:700;}
  .tl{color:var(--mint);font-weight:600;}

  .cover-title{font-weight:900;font-size:88px;line-height:1.05;letter-spacing:1px;text-transform:uppercase;color:#fff;}
  .rule{width:120px;height:6px;background:linear-gradient(90deg,var(--amber),var(--teal));border-radius:3px;margin:46px 0 40px;}
  .cover-sub{font-weight:500;font-size:44px;line-height:1.4;color:#B9C6C9;max-width:820px;}
  .swipe{margin-top:64px;font-weight:600;font-size:28px;color:var(--dim);letter-spacing:1px;}
  .swipe span{color:var(--amber);margin-left:6px;font-size:32px;}

  .body-title{font-weight:800;font-size:52px;line-height:1.16;letter-spacing:1px;text-transform:uppercase;color:#fff;margin-bottom:36px;}
  .body-text{font-weight:500;font-size:52px;line-height:1.42;color:#DCE6E8;}
  .cite{margin-top:48px;font-weight:600;font-size:26px;letter-spacing:0.5px;color:var(--dim);padding-left:22px;border-left:3px solid var(--teal);}

  /* list */
  .list{list-style:none;margin-top:14px;}
  .list li{display:flex;align-items:flex-start;gap:30px;padding:30px 0;border-bottom:1px solid rgba(204,251,241,0.08);}
  .list li:last-child{border-bottom:none;}
  .num{font-weight:800;font-size:34px;color:var(--teal);min-width:56px;padding-top:6px;}
  .li-txt{font-weight:500;font-size:50px;line-height:1.25;color:#DCE6E8;}

  /* cta */
  .cta-title{font-weight:900;font-size:84px;line-height:1.04;letter-spacing:1px;text-transform:uppercase;color:#fff;margin-bottom:40px;}
  .cta-btn{
    margin-top:64px;align-self:flex-start;display:inline-flex;align-items:center;gap:18px;
    background:linear-gradient(135deg,var(--amber),#EA8C0A);
    color:#20160a;font-weight:800;font-size:40px;letter-spacing:0.5px;
    padding:30px 52px;border-radius:100px;
    box-shadow:0 16px 44px rgba(245,158,11,0.32);
  }
  .cta-btn .arr{font-size:42px;}

  /* bottom bar */
  .botbar{display:flex;align-items:center;justify-content:space-between;}
  .url{font-weight:600;font-size:26px;letter-spacing:3px;color:var(--dim);text-transform:uppercase;}
  .dots{display:flex;gap:12px;}
  .dot{width:11px;height:11px;border-radius:50%;background:rgba(204,251,241,0.18);}
  .dot.on{background:var(--amber);width:34px;border-radius:6px;box-shadow:0 0 16px rgba(245,158,11,0.5);}
  </style></head>
  <body><div class="frame">
    ${c.top}
    ${slideInner(s, idx)}
    ${c.bottom}
  </div></body></html>`;
}

module.exports = { renderSlide, TOTAL };
