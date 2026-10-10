
(function(){
"use strict";
var root=document.documentElement,themeBtn=document.getElementById("theme-toggle"),menuBtn=document.getElementById("menu-toggle"),nav=document.getElementById("main-nav"),overlay=document.getElementById("mobile-overlay");
function applyTheme(t){root.dataset.theme=t; if(themeBtn){themeBtn.textContent=t==="dark"?"☀":"☾";themeBtn.setAttribute("aria-label",t==="dark"?"切换浅色模式":"切换深色模式");}}
var saved=null;try{saved=localStorage.getItem("zh-theme")}catch(e){}
applyTheme(saved==="light"||saved==="dark"?saved:window.matchMedia&&window.matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light");
if(themeBtn)themeBtn.addEventListener("click",function(){var t=root.dataset.theme==="dark"?"light":"dark";applyTheme(t);try{localStorage.setItem("zh-theme",t)}catch(e){}});
function closeDrops(){document.querySelectorAll(".nav-item.open").forEach(function(n){n.classList.remove("open");var b=n.querySelector(".nav-drop-toggle");if(b)b.setAttribute("aria-expanded","false")});}
function closeMenu(){if(!nav)return;nav.classList.remove("mobile-open");overlay.classList.remove("active");menuBtn.setAttribute("aria-expanded","false");menuBtn.textContent="☰";document.body.style.overflow="";closeDrops();}
if(menuBtn)menuBtn.addEventListener("click",function(){var open=nav.classList.contains("mobile-open");if(open)closeMenu();else{nav.classList.add("mobile-open");overlay.classList.add("active");menuBtn.textContent="✕";menuBtn.setAttribute("aria-expanded","true");document.body.style.overflow="hidden";}});
if(overlay)overlay.addEventListener("click",closeMenu);
document.querySelectorAll(".nav-drop-toggle").forEach(function(b){b.addEventListener("click",function(){var item=b.closest(".nav-item"),opening=!item.classList.contains("open");closeDrops();if(opening){item.classList.add("open");b.setAttribute("aria-expanded","true");}})});
if(nav)nav.querySelectorAll("a").forEach(function(a){a.addEventListener("click",closeMenu)});
document.addEventListener("keydown",function(e){if(e.key==="Escape"){closeMenu();closeDrops();}});
document.addEventListener("click",function(e){if(!e.target.closest(".nav-item"))closeDrops();});
window.addEventListener("resize",function(){if(window.innerWidth>1500)closeMenu();});
var side=document.querySelector(".side-details");if(side){var mobile=window.innerWidth<=940;side.open=!mobile;window.addEventListener("resize",function(){var m=window.innerWidth<=940;if(m!==mobile){mobile=m;side.open=!m;}});side.querySelectorAll("a").forEach(function(a){a.addEventListener("click",function(){if(window.innerWidth<=940)side.open=false;})});}
var model=document.getElementById("vehicle"),unit=document.getElementById("period"),count=document.getElementById("quantity"),amount=document.getElementById("estimate-amount"),deposit=document.getElementById("estimate-deposit");
if(model&&unit&&count&&amount&&deposit){
var source=document.getElementById("pricing-data"),rates=[];try{rates=JSON.parse(source?source.textContent:"[]")}catch(e){};if(!Array.isArray(rates)||rates.length===0){amount.textContent="请联系门店报价";return;}var fmt=function(v){return new Intl.NumberFormat("en-US").format(v)+" ₫"};
var update=function(){var v=rates[Number(model.value)],period=unit.value,q=Number(count.value);if(!Number.isFinite(q)||q<1){q=1};q=Math.min(365,Math.floor(q));if(Number(count.value)!==q)count.value=q;var rate=v[period];if(!rate){amount.textContent="请联系门店报价";deposit.textContent="押金： "+v.deposit;return;}var lo=rate[0]*q,hi=rate[1]*q;amount.textContent=lo===hi?fmt(lo):fmt(lo)+" – "+fmt(hi);deposit.textContent="参考押金（另计）： "+v.deposit;};
[model,unit,count].forEach(function(x){x.addEventListener("input",update);x.addEventListener("change",update)});update();
}
})();