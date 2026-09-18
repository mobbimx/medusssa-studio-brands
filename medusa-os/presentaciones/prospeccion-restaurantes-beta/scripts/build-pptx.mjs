// Genera deck-editable.pptx (9 slides) con pptxgenjs.
// Requiere: npm i pptxgenjs   ·   Uso: node scripts/build-pptx.mjs
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
const require = createRequire(import.meta.url);
let PptxGen;
for (const c of ['pptxgenjs','/opt/node22/lib/node_modules/pptxgenjs']) { try { PptxGen = require(c); break; } catch {} }
if (!PptxGen) { console.error('Falta pptxgenjs. Instala con: npm i pptxgenjs'); process.exit(1); }

const HERE = path.dirname(fileURLToPath(import.meta.url));
const A = path.resolve(HERE, '..', 'assets-pptx');
const OUT = path.resolve(HERE, '..', 'deck-editable.pptx');

// palette (no #)
const C = {
  ink:'0C0E29', ink2:'141738', violet:'6D5CEF', violet2:'8F80FF', cyan:'28D7EE',
  teal:'12B39B', magenta:'F2568A', gold:'FFCE5A', goldTx:'FFC24D', paper2:'F4F5FC',
  line:'E6E7F5', lineD:'2B2F63', tx:'14152E', tx2:'565986', tx3:'8B8EB4',
  txD:'EEF0FF', txD2:'A7ABE0', coral:'ED6864', white:'FFFFFF'
};
const FH = 'Space Grotesk', FB = 'Inter';
const M = 0.62;                 // side margin
const W = 13.333, H = 7.5, CW = W - 2*M;

const p = new PptxGen();
p.layout = 'LAYOUT_WIDE';

function bg(s, color){ s.background = { color }; }
function eyebrow(s, t, x, y, dark){
  s.addText(t.toUpperCase(), { isTextBox:true, x, y, w:8, h:0.3, fontFace:FH, bold:true,
    fontSize:12, charSpacing:3, color: dark?C.cyan:C.violet, align:'left', valign:'middle', margin:0 });
}
function footer(s, label, dark){
  s.addText('MedusaOS · Panel promocional', { isTextBox:true, x:M, y:7.02, w:6, h:0.3,
    fontFace:FH, bold:true, fontSize:10, color: dark?C.txD2:C.tx2, align:'left', valign:'middle', margin:0 });
  s.addText(label, { isTextBox:true, x:W-M-5, y:7.02, w:5, h:0.3,
    fontFace:FB, fontSize:10, color: dark?'7A7EB8':C.tx3, align:'right', valign:'middle', margin:0 });
}
function glow(s, x, y, d, color, tr){
  s.addShape(p.ShapeType.ellipse, { x, y, w:d, h:d, fill:{ color, transparency: tr }, line:{ type:'none' } });
}
function card(s, x, y, w, h, fill, lineColor){
  s.addShape(p.ShapeType.roundRect, { x, y, w, h, rectRadius:0.12,
    fill:{ color:fill }, line: lineColor?{ color:lineColor, width:1 }:{ type:'none' } });
}
function badge(s, t, x, y, w, fill, txc){
  s.addShape(p.ShapeType.roundRect, { x, y, w, h:0.4, rectRadius:0.2, fill:{ color:fill }, line:{ type:'none' } });
  s.addText(t, { isTextBox:true, x, y, w, h:0.4, fontFace:FH, bold:true, fontSize:11.5, charSpacing:1.5,
    color:txc, align:'center', valign:'middle', margin:0 });
}

/* ===== 1 · PORTADA ===== */
{
  const s = p.addSlide(); bg(s, C.ink);
  glow(s, 8.6, -1.6, 5.6, C.violet, 55);
  glow(s, -1.6, 4.8, 4.6, C.cyan, 70);
  s.addImage({ path:`${A}/mark.png`, x:M, y:0.52, w:0.44, h:0.44 });
  s.addText([
    { text:'Medusa', options:{ color:C.txD } }, { text:'OS', options:{ color:C.violet2 } }
  ], { isTextBox:true, x:1.14, y:0.44, w:4, h:0.36, fontFace:FH, bold:true, fontSize:18, valign:'middle', margin:0 });
  s.addText('PANEL PROMOCIONAL', { isTextBox:true, x:1.15, y:0.8, w:4, h:0.24, fontFace:FH, fontSize:9,
    charSpacing:4, color:C.tx3, valign:'middle', margin:0 });

  badge(s, '✦  PRUEBA BETA', M, 2.05, 2.0, C.gold, '3A2600');
  s.addText('GRATIS', { isTextBox:true, x:M-0.04, y:2.42, w:7.4, h:1.8, fontFace:FH, bold:true,
    fontSize:118, color:C.goldTx, align:'left', valign:'middle', margin:0 });
  s.addText('para los primeros negocios de la zona', { isTextBox:true, x:8.05, y:3.15, w:4.5, h:1.2,
    fontFace:FH, bold:true, fontSize:22, color:C.txD, align:'left', valign:'middle', margin:0 });

  s.addText([
    { text:'Publicidad local ', options:{ color:C.txD2 } },
    { text:'medible', options:{ color:C.txD, bold:true } },
    { text:' para negocios de la zona: te ponemos frente a la gente que anda cerca, la ', options:{ color:C.txD2 } },
    { text:'redirigimos a tu negocio', options:{ color:C.txD, bold:true } },
    { text:' y te mostramos ', options:{ color:C.txD2 } },
    { text:'exactamente qué funciona', options:{ color:C.txD, bold:true } },
    { text:'.', options:{ color:C.txD2 } }
  ], { isTextBox:true, x:M, y:4.7, w:9.4, h:1.3, fontFace:FB, fontSize:18, lineSpacingMultiple:1.3, align:'left', valign:'top', margin:0 });

  s.addShape(p.ShapeType.roundRect, { x:M, y:6.62, w:4.9, h:0.42, rectRadius:0.21, fill:{ type:'none' }, line:{ color:C.lineD, width:1 } });
  s.addText('ANCLADO A LA SEDE DE MOBBITRIPS · XALAPA', { isTextBox:true, x:M, y:6.62, w:4.9, h:0.42,
    fontFace:FH, bold:true, fontSize:10.5, charSpacing:1, color:C.txD2, align:'center', valign:'middle', margin:0 });
  s.addText([
    { text:'Presenta: ', options:{ color:C.txD2 } }, { text:'Medusssa Studio', options:{ color:C.txD, bold:true } }
  ], { isTextBox:true, x:5.75, y:6.62, w:5, h:0.42, fontFace:FB, fontSize:13, valign:'middle', margin:0 });
  s.addNotes('Enganchar con la oferta GRATIS y "medible". Beta gratuita para los primeros negocios de la zona. No explicar el producto todavía.');
}

/* ===== 2 · LA OPORTUNIDAD ===== */
{
  const s = p.addSlide(); bg(s, C.white);
  eyebrow(s, 'La oportunidad', M, 0.62, false);
  s.addText('Tus mejores clientes ya están a menos de 1 km.', { isTextBox:true, x:M, y:1.05, w:6.6, h:1.5,
    fontFace:FH, bold:true, fontSize:38, color:C.tx, lineSpacingMultiple:1.05, align:'left', valign:'top', margin:0 });
  s.addText([
    { text:'Huéspedes de ', options:{ color:C.tx2 } }, { text:'Mobbitrips', options:{ color:C.coral, bold:true } },
    { text:', vecinos, oficinas y gente de paso se preguntan todos los días lo mismo: ', options:{ color:C.tx2 } },
    { text:'“¿dónde como algo rico aquí cerca?”', options:{ color:C.tx, bold:true } }
  ], { isTextBox:true, x:M, y:2.75, w:6.5, h:1.3, fontFace:FB, fontSize:17, lineSpacingMultiple:1.3, valign:'top', margin:0 });
  s.addText([
    { text:'Hoy esa decisión se la lleva la suerte. Nosotros la ponemos frente a ellos — ', options:{ color:C.tx2 } },
    { text:'a tu favor', options:{ color:C.tx, bold:true } }, { text:'.', options:{ color:C.tx2 } }
  ], { isTextBox:true, x:M, y:4.05, w:6.5, h:1.0, fontFace:FB, fontSize:17, lineSpacingMultiple:1.3, valign:'top', margin:0 });
  const stats = [['1 km','radio de la beta'],['100%','público local y real'],['0','comisión por venta']];
  stats.forEach((st,i)=>{
    const x = M + i*2.15;
    s.addText(st[0], { isTextBox:true, x, y:5.25, w:2.0, h:0.55, fontFace:FH, bold:true, fontSize:32, color:C.violet, align:'left', valign:'middle', margin:0 });
    s.addText(st[1], { isTextBox:true, x, y:5.82, w:2.0, h:0.4, fontFace:FB, fontSize:12, color:C.tx2, align:'left', valign:'top', margin:0 });
  });
  s.addImage({ path:`${A}/map.png`, x:8.15, y:1.5, w:4.4, h:3.83 });
  footer(s, 'La oportunidad', false);
  s.addNotes('El cliente ya está cerca (huéspedes + vecinos + oficinas). Hoy gana la suerte; nosotros lo ponemos a tu favor. 1 km · público real · 0 comisión.');
}

/* ===== 3 · EL PROBLEMA ===== */
{
  const s = p.addSlide(); bg(s, C.white);
  eyebrow(s, 'El problema', M, 0.62, false);
  s.addText('Cada día pasan cientos de personas cerca de ti.\nCasi ninguna sabe que existes.', { isTextBox:true,
    x:M, y:1.02, w:11.5, h:1.5, fontFace:FH, bold:true, fontSize:34, color:C.tx, lineSpacingMultiple:1.06, valign:'top', margin:0 });
  const pains = [
    ['!','Publicidad que no puedes medir','Volantes, lonas y posts que pagas “a ciegas”: nunca sabes si de ahí llegó alguien.'],
    ['%','Las apps y comisiones te comen el margen','Comisiones del 20–30% por venta. Y el cliente termina siendo de la app, no tuyo.'],
    ['↓','Te gana quien sale primero en el mapa','Aunque tu oferta sea mejor, la decisión se la lleva quien aparece arriba en Google.']
  ];
  let y = 3.0;
  pains.forEach(pn=>{
    s.addShape(p.ShapeType.roundRect, { x:M, y:y+0.02, w:0.42, h:0.42, rectRadius:0.09, fill:{ color:'FBE1EA' }, line:{ type:'none' } });
    s.addText(pn[0], { isTextBox:true, x:M, y:y+0.02, w:0.42, h:0.42, fontFace:FH, bold:true, fontSize:16, color:C.magenta, align:'center', valign:'middle', margin:0 });
    s.addText(pn[1], { isTextBox:true, x:M+0.62, y:y-0.05, w:5.9, h:0.4, fontFace:FH, bold:true, fontSize:17.5, color:C.tx, valign:'middle', margin:0 });
    s.addText(pn[2], { isTextBox:true, x:M+0.62, y:y+0.36, w:5.9, h:0.7, fontFace:FB, fontSize:14, color:C.tx2, lineSpacingMultiple:1.25, valign:'top', margin:0 });
    y += 1.28;
  });
  // callout
  card(s, 7.35, 2.95, 5.35, 3.35, 'F7F0F7', 'F0D9E6');
  s.addText('EN UNA FRASE', { isTextBox:true, x:7.7, y:3.25, w:4.7, h:0.3, fontFace:FH, bold:true, fontSize:13, charSpacing:2, color:C.magenta, valign:'middle', margin:0 });
  s.addText('Gastas en publicidad sin saber si sirve — y compites por atención que ya estaba cerca de tu puerta.', { isTextBox:true,
    x:7.7, y:3.7, w:4.65, h:2.4, fontFace:FH, bold:true, fontSize:26, color:C.tx, lineSpacingMultiple:1.15, valign:'top', margin:0 });
  footer(s, 'El problema', false);
  s.addNotes('Que sienta el dolor: publicidad que no mide, comisiones, gana quien sale primero. Cierra: gastas sin saber si sirve.');
}

/* ===== 4 · QUÉ ES ===== */
{
  const s = p.addSlide(); bg(s, C.ink);
  glow(s, 5.5, -1.4, 3.8, C.violet, 62);
  eyebrow(s, 'Qué es', M, 0.95, true);
  s.addText([
    { text:'Un panel que recomienda tu negocio a la zona — y ', options:{ color:C.txD } },
    { text:'mide cada resultado', options:{ color:C.cyan } }, { text:'.', options:{ color:C.txD } }
  ], { isTextBox:true, x:M, y:1.4, w:11.6, h:1.5, fontFace:FH, bold:true, fontSize:36, lineSpacingMultiple:1.06, valign:'top', margin:0 });
  const pil = [
    ['ic_vitrina.png','Vitrina digital','Tu negocio, tu promo y tus fotos frente a clientes que están cerca.'],
    ['ic_redir.png','Redirección directa','Un escaneo y el cliente llega a tu WhatsApp, menú o ubicación. Sin intermediarios.'],
    ['ic_metrics.png','Métricas reales','Cuántos te vieron, cuántos escanearon y cuántos llegaron. Por fin, medible.']
  ];
  const cw = (CW - 2*0.35)/3;
  pil.forEach((c,i)=>{
    const x = M + i*(cw+0.35);
    card(s, x, 3.5, cw, 2.5, C.ink2, C.lineD);
    s.addShape(p.ShapeType.roundRect, { x:x+0.3, y:3.8, w:0.64, h:0.64, rectRadius:0.14, fill:{ color:'242a5e' }, line:{ type:'none' } });
    s.addImage({ path:`${A}/${c[0]}`, x:x+0.44, y:3.94, w:0.36, h:0.36 });
    s.addText(c[1], { isTextBox:true, x:x+0.3, y:4.6, w:cw-0.6, h:0.4, fontFace:FH, bold:true, fontSize:18, color:C.txD, valign:'middle', margin:0 });
    s.addText(c[2], { isTextBox:true, x:x+0.3, y:5.05, w:cw-0.6, h:0.9, fontFace:FB, fontSize:14, color:C.txD2, lineSpacingMultiple:1.3, valign:'top', margin:0 });
  });
  footer(s, 'Qué es', true);
  s.addNotes('Definición en una idea. Tres patas: vitrina digital, redirección directa, métricas reales.');
}

/* ===== 5 · EL PANEL EN PANTALLA ===== */
{
  const s = p.addSlide(); bg(s, C.white);
  eyebrow(s, 'El panel en pantalla', M, 0.6, false);
  s.addText('Así se ve en la pantalla.', { isTextBox:true, x:M, y:1.0, w:11, h:0.7, fontFace:FH, bold:true, fontSize:34, color:C.tx, valign:'middle', margin:0 });
  s.addText([
    { text:'El panel se proyecta en las pantallas de Mobbitrips. Hay dos vistas: la ', options:{ color:C.tx2 } },
    { text:'principal', options:{ color:C.tx, bold:true } }, { text:' y la de ', options:{ color:C.tx2 } },
    { text:'recomendaciones de la zona', options:{ color:C.tx, bold:true } }, { text:', donde aparece tu anuncio.', options:{ color:C.tx2 } }
  ], { isTextBox:true, x:M, y:1.72, w:11.8, h:0.6, fontFace:FB, fontSize:15, lineSpacingMultiple:1.25, valign:'top', margin:0 });

  const sw = (CW - 0.5)/2, sh = sw/1.82;
  const sy = 2.55;
  const screens = [['screen-principal.png','Pantalla principal',''],
                   ['screen-reco.png','Recomendaciones de la zona','Aquí aparece tu anuncio']];
  screens.forEach((sc,i)=>{
    const x = M + i*(sw+0.5);
    s.addImage({ path:`${A}/${sc[0]}`, x, y:sy, w:sw, h:sh });
    s.addShape(p.ShapeType.roundRect, { x, y:sy, w:sw, h:sh, rectRadius:0.08, fill:{ type:'none' }, line:{ color:'C9CCF0', width:1.25, dashType:'dash' } });
    // badge reemplazar bottom-right
    s.addShape(p.ShapeType.roundRect, { x:x+sw-2.55, y:sy+sh-0.5, w:2.4, h:0.34, rectRadius:0.17, fill:{ color:'FFF3CD' }, line:{ color:'E0A83C', width:1, dashType:'dash' } });
    s.addText('◆ REEMPLAZAR CON IMAGEN REAL', { isTextBox:true, x:x+sw-2.55, y:sy+sh-0.5, w:2.4, h:0.34, fontFace:FH, bold:true, fontSize:8.5, charSpacing:0.5, color:'8A5A00', align:'center', valign:'middle', margin:0 });
    s.addText(sc[1], { isTextBox:true, x, y:sy+sh+0.12, w:sw, h:0.32, fontFace:FH, bold:true, fontSize:15.5, color:C.tx, align:'center', valign:'middle', margin:0 });
    if (sc[2]) s.addText(sc[2], { isTextBox:true, x, y:sy+sh+0.44, w:sw, h:0.26, fontFace:FB, fontSize:12, color:C.tx3, align:'center', valign:'top', margin:0 });
  });
  footer(s, 'El panel en pantalla', false);
  s.addNotes('Que lo vea. Dos vistas: principal y recomendaciones (aquí aparece el anuncio). REEMPLAZAR los dos placeholders por las capturas reales.');
}

/* ===== 6 · EL FLUJO ===== */
{
  const s = p.addSlide(); bg(s, C.ink);
  glow(s, 8.5, -1.5, 4.2, C.violet, 66);
  eyebrow(s, 'El flujo', M, 0.62, true);
  s.addText([
    { text:'Del anuncio en pantalla ', options:{ color:C.txD } },
    { text:'a un cliente en tu negocio', options:{ color:C.cyan } }, { text:'.', options:{ color:C.txD } }
  ], { isTextBox:true, x:M, y:1.02, w:11.8, h:0.8, fontFace:FH, bold:true, fontSize:32, valign:'middle', margin:0 });

  const flow = [
    ['ic_tv.png','PASO 1','Se proyecta en la tele','El anuncio aparece en la pantalla y el huésped consume la publicidad.', false],
    ['ic_menu.png','PASO 2','Conoce el negocio','Ve la información: menú, cómo llegar e imágenes.', false],
    ['ic_qr.png','PASO 3','Escanea el QR','Lo redirige a comunicación directa contigo, vinculada a la promoción.', false],
    ['ic_store.png','RESULTADO','Llega al negocio','El cliente llega a tu local o cierra un pedido contigo.', true]
  ];
  const gap = 0.42, cw = (CW - 3*gap)/4, cy = 2.35, ch = 3.05;
  flow.forEach((f,i)=>{
    const x = M + i*(cw+gap);
    card(s, x, cy, cw, ch, f[4]?'123a33':C.ink2, f[4]?'1F6B5E':C.lineD);
    s.addImage({ path:`${A}/${f[0]}`, x:x+cw/2-0.33, y:cy+0.28, w:0.66, h:0.66 });
    s.addText(f[1], { isTextBox:true, x:x+0.15, y:cy+1.05, w:cw-0.3, h:0.28, fontFace:FH, bold:true, fontSize:11.5, charSpacing:1.5, color:f[4]?C.teal:C.cyan, align:'center', valign:'middle', margin:0 });
    s.addText(f[2], { isTextBox:true, x:x+0.15, y:cy+1.35, w:cw-0.3, h:0.5, fontFace:FH, bold:true, fontSize:16, color:C.txD, align:'center', valign:'top', lineSpacingMultiple:1.05, margin:0 });
    s.addText(f[3], { isTextBox:true, x:x+0.16, y:cy+1.9, w:cw-0.32, h:1.05, fontFace:FB, fontSize:12, color:C.txD2, align:'center', valign:'top', lineSpacingMultiple:1.2, margin:0 });
    if (i<3) s.addText('→', { isTextBox:true, x:x+cw-0.02, y:cy, w:gap+0.04, h:ch, fontFace:FB, fontSize:22, color:C.violet2, align:'center', valign:'middle', margin:0 });
  });
  card(s, M, 5.75, CW, 0.8, C.ink2, C.lineD);
  badge(s, 'SIN COMISIÓN', M+0.25, 5.95, 1.7, C.teal, '022B25');
  s.addText([
    { text:'Todo va ', options:{ color:C.txD2 } }, { text:'vinculado a tu promoción', options:{ color:C.txD, bold:true } },
    { text:' y el contacto llega directo a ti. No cobramos por venta.', options:{ color:C.txD2 } }
  ], { isTextBox:true, x:M+2.15, y:5.75, w:CW-2.4, h:0.8, fontFace:FB, fontSize:15, valign:'middle', margin:0 });
  footer(s, 'El flujo', true);
  s.addNotes('Paso 1 proyecta en TV. Paso 2 conoce el negocio (menú/cómo llegar/imágenes). Paso 3 escanea QR -> contacto directo vinculado a la promo. Resultado: llega o cierra pedido. Sin comisión.');
}

/* ===== 7 · LAS MÉTRICAS ===== */
{
  const s = p.addSlide(); bg(s, C.white);
  eyebrow(s, 'Las métricas', M, 0.55, false);
  s.addText([
    { text:'Por fin vas a saber ', options:{ color:C.tx } }, { text:'qué está funcionando', options:{ color:C.violet } }, { text:'.', options:{ color:C.tx } }
  ], { isTextBox:true, x:M, y:0.95, w:7, h:1.3, fontFace:FH, bold:true, fontSize:32, lineSpacingMultiple:1.05, valign:'top', margin:0 });
  s.addShape(p.ShapeType.roundRect, { x:7.75, y:1.02, w:4.95, h:0.42, rectRadius:0.1, fill:{ color:'FFF3CD' }, line:{ color:'E0A83C', width:1, dashType:'dash' } });
  s.addText('◆ MOCKUP · REEMPLAZAR CON CAPTURA REAL DEL DASHBOARD', { isTextBox:true, x:7.75, y:1.02, w:4.95, h:0.42, fontFace:FH, bold:true, fontSize:9, charSpacing:0.5, color:'8A5A00', align:'center', valign:'middle', margin:0 });
  s.addImage({ path:`${A}/dashboard.png`, x:M, y:1.78, w:CW, h:CW/2.617 });
  s.addText([
    { text:'Cada bimestre te llega un ', options:{ color:C.tx2 } }, { text:'reporte simple', options:{ color:C.tx, bold:true } },
    { text:': cuánta gente te vio, qué promo funcionó y a qué hora conviene publicar.', options:{ color:C.tx2 } }
  ], { isTextBox:true, x:M, y:6.45, w:CW, h:0.35, fontFace:FB, fontSize:13, valign:'middle', margin:0 });
  footer(s, 'Las métricas', false);
  s.addNotes('El corazón del pitch: es medible. Embudo impresiones->escaneos->redirecciones, horarios pico, top promo. REEMPLAZAR por captura real. Reporte bimestral.');
}

/* ===== 8 · BETA GRATIS ===== */
{
  const s = p.addSlide(); bg(s, C.ink);
  glow(s, 9.2, -1.6, 4.2, C.gold, 82);
  badge(s, 'PRUEBA BETA', M, 0.6, 1.85, C.gold, '3A2600');
  badge(s, '100% GRATIS', M+2.0, 0.6, 1.75, C.teal, '022B25');
  s.addText('Sé de los primeros. Sin costo, sin tarjeta, sin compromiso.', { isTextBox:true, x:M, y:1.18, w:11.8, h:1.0,
    fontFace:FH, bold:true, fontSize:31, color:C.txD, lineSpacingMultiple:1.05, valign:'top', margin:0 });
  const checks = [
    ['Tu negocio en el panel — gratis','Ficha con fotos y promo durante todo el periodo beta.'],
    ['Redirección a WhatsApp, menú y mapa','Los clientes llegan directo a ti, sin comisión por venta.'],
    ['Reporte de métricas bimestral','Datos reales de cuánta gente te vio y te buscó.'],
    ['Nosotros armamos tu ficha','Tú solo mandas fotos y promo; del resto nos encargamos.']
  ];
  let y = 2.45;
  checks.forEach(ck=>{
    s.addShape(p.ShapeType.roundRect, { x:M, y, w:0.44, h:0.44, rectRadius:0.1, fill:{ color:C.gold }, line:{ type:'none' } });
    s.addText('✓', { isTextBox:true, x:M, y, w:0.44, h:0.44, fontFace:FH, bold:true, fontSize:18, color:'3A2600', align:'center', valign:'middle', margin:0 });
    s.addText(ck[0], { isTextBox:true, x:M+0.62, y:y-0.06, w:5.7, h:0.4, fontFace:FH, bold:true, fontSize:17, color:C.txD, valign:'middle', margin:0 });
    s.addText(ck[1], { isTextBox:true, x:M+0.62, y:y+0.32, w:5.7, h:0.5, fontFace:FB, fontSize:13.5, color:C.txD2, lineSpacingMultiple:1.2, valign:'top', margin:0 });
    y += 1.02;
  });
  card(s, 7.35, 2.45, 5.35, 3.7, '20204a', '4A3A2A');
  s.addText('CUPO LIMITADO POR ZONA', { isTextBox:true, x:7.7, y:2.78, w:4.7, h:0.3, fontFace:FH, bold:true, fontSize:13, charSpacing:2, color:C.gold, valign:'middle', margin:0 });
  s.addText('Aceptamos pocos negocios por categoría dentro del radio de 1 km.', { isTextBox:true, x:7.7, y:3.2, w:4.65, h:1.3,
    fontFace:FH, bold:true, fontSize:24, color:C.txD, lineSpacingMultiple:1.15, valign:'top', margin:0 });
  s.addText([
    { text:'No saturamos el panel: cuidamos que tu promo destaque. El que entra en la beta ', options:{ color:C.txD2 } },
    { text:'se queda con el lugar', options:{ color:C.gold, bold:true } }, { text:' de su categoría en la zona.', options:{ color:C.txD2 } }
  ], { isTextBox:true, x:7.7, y:4.65, w:4.65, h:1.1, fontFace:FB, fontSize:14, lineSpacingMultiple:1.3, valign:'top', margin:0 });
  footer(s, 'Prueba beta gratuita', true);
  s.addNotes('Gratis, sin riesgo, con CUPO por categoría. El que entra se queda con el lugar de su zona. Reporte bimestral. Bajar el ritmo: esta convierte.');
}

/* ===== 9 · CÓMO EMPIEZAS (cierre) ===== */
{
  const s = p.addSlide(); bg(s, C.ink);
  glow(s, -1.6, 4.6, 5.0, C.violet, 60);
  eyebrow(s, 'Cómo empiezas', M, 0.75, true);
  s.addText('En 15 minutos estás dentro.', { isTextBox:true, x:M, y:1.15, w:11, h:0.8, fontFace:FH, bold:true, fontSize:38, color:C.txD, valign:'middle', margin:0 });
  const steps = [
    ['1','Nos das lo básico','Nombre, 3–5 fotos, tu promo de arranque y a dónde mandamos a los clientes (WhatsApp, menú o ubicación).'],
    ['2','Armamos tu ficha','Nosotros la diseñamos y la dejamos lista en el panel. Tú la apruebas. Cero trabajo técnico de tu lado.'],
    ['3','Publicamos y mides','Tu negocio entra al panel de la zona y empiezas a recibir clientes — y tu primer reporte.']
  ];
  const cw = (CW - 2*0.35)/3;
  steps.forEach((st,i)=>{
    const x = M + i*(cw+0.35);
    card(s, x, 2.5, cw, 2.55, C.ink2, C.lineD);
    s.addShape(p.ShapeType.roundRect, { x:x+0.3, y:2.8, w:0.58, h:0.58, rectRadius:0.13, fill:{ color:C.violet }, line:{ type:'none' } });
    s.addText(st[0], { isTextBox:true, x:x+0.3, y:2.8, w:0.58, h:0.58, fontFace:FH, bold:true, fontSize:22, color:C.white, align:'center', valign:'middle', margin:0 });
    s.addText(st[1], { isTextBox:true, x:x+1.0, y:2.82, w:cw-1.2, h:0.55, fontFace:FH, bold:true, fontSize:17, color:C.txD, valign:'middle', margin:0 });
    s.addText(st[2], { isTextBox:true, x:x+0.3, y:3.6, w:cw-0.6, h:1.2, fontFace:FB, fontSize:13.5, color:C.txD2, lineSpacingMultiple:1.3, valign:'top', margin:0 });
  });
  s.addShape(p.ShapeType.roundRect, { x:M, y:5.5, w:3.9, h:0.7, rectRadius:0.14, fill:{ color:C.violet }, line:{ type:'none' } });
  s.addText('Aparta tu lugar en la beta  →', { isTextBox:true, x:M, y:5.5, w:3.9, h:0.7, fontFace:FH, bold:true, fontSize:17, color:C.white, align:'center', valign:'middle', margin:0 });
  s.addText('Solo para negocios a 1 km de la sede de Mobbitrips.', { isTextBox:true, x:M+4.15, y:5.5, w:6, h:0.7, fontFace:FB, fontSize:15, color:C.txD2, valign:'middle', margin:0 });
  footer(s, 'Cómo empiezas', true);
  s.addNotes('Quitar fricción: tú solo mandas fotos y promo. Cerrar pidiendo nombre, WhatsApp y compromiso de fotos. Agendar el día.');
}

await p.writeFile({ fileName: OUT });
console.log('PPTX ->', OUT);
