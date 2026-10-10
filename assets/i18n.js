---
layout: null
---
/* Chinese-first bilingual UI. Source HTML stays zh-CN and SEO/canonical remain unchanged.
   English is a curated, client-side presentation layer with no external API. */
(function () {
  "use strict";
  var translations = {{ site.data["i18n-en"] | jsonify }};
  var toggle = document.getElementById("language-toggle");
  if (!toggle || !translations) return;
  var storageKey = "china-ui-language";
  var sorted = Object.keys(translations).filter(Boolean).sort(function (a,b) { return b.length-a.length; });
  var trackedText = new WeakMap();
  var trackedAttrs = new WeakMap();
  var language = "zh";
  var hasChinese = /[\u3400-\u9fff]/;
  function englishText(value) {
    if (!hasChinese.test(value)) return value;
    var clean=value.trim(), result=translations[clean];
    if (typeof result==="string") return value.replace(clean,result);
    // Previews on the homepage are shortened to ~70 Chinese characters.
    if (/[…]$/.test(clean)) {
      var partial=clean.slice(0,-1);
      for (var i=0;i<sorted.length;i++) {
        var key=sorted[i];
        if (partial.length>=15 && key.length>partial.length && key.indexOf(partial)===0) {
          return value.replace(clean,translations[key].slice(0,148)+"…");
        }
      }
    }
    var output=clean;
    for (var j=0;j<sorted.length;j++){
      var k=sorted[j];
      if (output.indexOf(k)!==-1) output=output.split(k).join(translations[k]);
    }
    return value.replace(clean,output);
  }
  function attrEnglish(name, value) {
    if (name==="aria-label"){
      var submenu=value.match(/^展开(.+)子分类$/);
      if(submenu) return "Expand "+englishText(submenu[1])+" subcategories";
    }
    return englishText(value);
  }
  function updateText(node){
    var state=trackedText.get(node);
    if(!state) {state={zh:node.nodeValue,last:node.nodeValue}; trackedText.set(node,state);}
    else if(node.nodeValue!==state.last){state.zh=node.nodeValue;}
    var next=language==="en"?englishText(state.zh):state.zh;
    if(node.nodeValue!==next) node.nodeValue=next;
    state.last=next;
  }
  function updateAttributes(el){
    var keys=["aria-label","title","placeholder","alt"];
    var stored=trackedAttrs.get(el) || {};
    keys.forEach(function(attr){
      if(!el.hasAttribute(attr))return;
      var live=el.getAttribute(attr), state=stored[attr];
      if(!state){state={zh:live,last:live};stored[attr]=state;}
      else if(live!==state.last){state.zh=live;}
      var next=language==="en"?attrEnglish(attr,state.zh):state.zh;
      if(live!==next)el.setAttribute(attr,next);
      state.last=next;
    });
    trackedAttrs.set(el,stored);
  }
  function refresh(){
    // Translate visible user interface only. Keep metadata, JSON-LD and links intact.
    var walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,{
      acceptNode:function(n){
        var el=n.parentElement;
        if(!el || el.closest("script,style,noscript,svg,pre,code,#language-toggle,[translate='no']"))
          return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var nodes=[];while(walker.nextNode())nodes.push(walker.currentNode);
    nodes.forEach(updateText);
    document.body.querySelectorAll("[aria-label],[title],[placeholder],[alt]").forEach(function(el){
      if(!el.closest("#language-toggle,[translate='no']"))updateAttributes(el);
    });
  }
  function setLanguage(next){
    language=next==="en"?"en":"zh";
    document.documentElement.lang=language==="en"?"en":"zh-CN";
    document.documentElement.setAttribute("data-ui-lang",language);
    toggle.setAttribute("aria-label",language==="en"?"Switch to Chinese":"Switch to English");
    toggle.setAttribute("aria-pressed",language==="en"?"true":"false");
    refresh();
    try{localStorage.setItem(storageKey,language)}catch(e){}
  }
  toggle.addEventListener("click",function(){setLanguage(language==="en"?"zh":"en");});
  // The rental calculator updates text after user input, so reapply the selected language.
  ["vehicle","period","quantity"].forEach(function(id){
    var el=document.getElementById(id);
    if(el){el.addEventListener("input",refresh);el.addEventListener("change",refresh);}
  });
  try{language=localStorage.getItem(storageKey)==="en"?"en":"zh";}catch(e){language="zh";}
  setLanguage(language);
  window.chinaLanguage={set:setLanguage,get:function(){return language;},refresh:refresh};
})();