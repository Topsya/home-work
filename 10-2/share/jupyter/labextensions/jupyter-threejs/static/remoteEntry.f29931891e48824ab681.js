var _JUPYTERLAB;(()=>{"use strict";var e,r,t,a,n,o,i,d,u,l,f,s,c,h,p,v,b,m,g={1437:(e,r,t)=>{var a={"./index":()=>Promise.all([t.e(725),t.e(590)]).then((()=>()=>t(5590))),"./extension":()=>Promise.all([t.e(725),t.e(738)]).then((()=>()=>t(3738)))},n=(e,r)=>(t.R=r,r=t.o(a,e)?a[e]():Promise.resolve().then((()=>{throw new Error('Module "'+e+'" does not exist in container.')})),t.R=void 0,r),o=(e,r)=>{if(t.S){var a="default",n=t.S[a];if(n&&n!==e)throw new Error("Container initialization failed as it has already been initialized with a different share scope");return t.S[a]=e,t.I(a,r)}};t.d(r,{get:()=>n,init:()=>o})}},y={};function j(e){var r=y[e];if(void 0!==r)return r.exports;var t=y[e]={id:e,loaded:!1,exports:{}};return g[e].call(t.exports,t,t.exports,j),t.loaded=!0,t.exports}j.m=g,j.c=y,j.n=e=>{var r=e&&e.__esModule?()=>e.default:()=>e;return j.d(r,{a:r}),r},j.d=(e,r)=>{for(var t in r)j.o(r,t)&&!j.o(e,t)&&Object.defineProperty(e,t,{enumerable:!0,get:r[t]})},j.f={},j.e=e=>Promise.all(Object.keys(j.f).reduce(((r,t)=>(j.f[t](e,r),r)),[])),j.u=e=>(398===e?"jupyter-threejs-chunk":e)+"."+{170:"cd85d35f0d876cdac13a",212:"28988830f14c6406a07b",270:"f09e82a7948794e8fe7c",398:"75bff6c5b3e16e2f7d65",590:"40e4a9ac0f4f57864769",624:"12b52bd1c970e314e741",725:"598aa99405a87ad5fae1",738:"28fb39dcba9e2575f78a",794:"6dae22c163628400884b",822:"27544b4e4c01436d6f8d",861:"5d5b0ba33675d668ca0c"}[e]+".js?v="+{170:"cd85d35f0d876cdac13a",212:"28988830f14c6406a07b",270:"f09e82a7948794e8fe7c",398:"75bff6c5b3e16e2f7d65",590:"40e4a9ac0f4f57864769",624:"12b52bd1c970e314e741",725:"598aa99405a87ad5fae1",738:"28fb39dcba9e2575f78a",794:"6dae22c163628400884b",822:"27544b4e4c01436d6f8d",861:"5d5b0ba33675d668ca0c"}[e],j.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),j.o=(e,r)=>Object.prototype.hasOwnProperty.call(e,r),e={},r="jupyter-threejs:",j.l=(t,a,n,o)=>{if(e[t])e[t].push(a);else{var i,d;if(void 0!==n)for(var u=document.getElementsByTagName("script"),l=0;l<u.length;l++){var f=u[l];if(f.getAttribute("src")==t||f.getAttribute("data-webpack")==r+n){i=f;break}}i||(d=!0,(i=document.createElement("script")).charset="utf-8",i.timeout=120,j.nc&&i.setAttribute("nonce",j.nc),i.setAttribute("data-webpack",r+n),i.src=t),e[t]=[a];var s=(r,a)=>{i.onerror=i.onload=null,clearTimeout(c);var n=e[t];if(delete e[t],i.parentNode&&i.parentNode.removeChild(i),n&&n.forEach((e=>e(a))),r)return r(a)},c=setTimeout(s.bind(null,void 0,{type:"timeout",target:i}),12e4);i.onerror=s.bind(null,i.onerror),i.onload=s.bind(null,i.onload),d&&document.head.appendChild(i)}},j.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},j.nmd=e=>(e.paths=[],e.children||(e.children=[]),e),(()=>{j.S={};var e={},r={};j.I=(t,a)=>{a||(a=[]);var n=r[t];if(n||(n=r[t]={}),!(a.indexOf(n)>=0)){if(a.push(n),e[t])return e[t];j.o(j.S,t)||(j.S[t]={});var o=j.S[t],i="jupyter-threejs",d=(e,r,t,a)=>{var n=o[e]=o[e]||{},d=n[r];(!d||!d.loaded&&(!a!=!d.eager?a:i>d.from))&&(n[r]={get:t,from:i,eager:!!a})},u=[];return"default"===t&&(d("bluebird","3.7.2",(()=>j.e(624).then((()=>()=>j(6624))))),d("jupyter-dataserializers","3.0.1",(()=>Promise.all([j.e(822),j.e(170),j.e(861)]).then((()=>()=>j(6822))))),d("jupyter-threejs","2.4.1",(()=>Promise.all([j.e(725),j.e(590)]).then((()=>()=>j(5590))))),d("three","0.97.0",(()=>j.e(212).then((()=>()=>j(2212))))),d("underscore","1.13.6",(()=>j.e(794).then((()=>()=>j(7794)))))),e[t]=u.length?Promise.all(u).then((()=>e[t]=1)):1}}})(),(()=>{var e;j.g.importScripts&&(e=j.g.location+"");var r=j.g.document;if(!e&&r&&(r.currentScript&&(e=r.currentScript.src),!e)){var t=r.getElementsByTagName("script");t.length&&(e=t[t.length-1].src)}if(!e)throw new Error("Automatic publicPath is not supported in this browser");e=e.replace(/#.*$/,"").replace(/\?.*$/,"").replace(/\/[^\/]+$/,"/"),j.p=e})(),t=e=>{var r=e=>e.split(".").map((e=>+e==e?+e:e)),t=/^([^-+]+)?(?:-([^+]+))?(?:\+(.+))?$/.exec(e),a=t[1]?r(t[1]):[];return t[2]&&(a.length++,a.push.apply(a,r(t[2]))),t[3]&&(a.push([]),a.push.apply(a,r(t[3]))),a},a=(e,r)=>{e=t(e),r=t(r);for(var a=0;;){if(a>=e.length)return a<r.length&&"u"!=(typeof r[a])[0];var n=e[a],o=(typeof n)[0];if(a>=r.length)return"u"==o;var i=r[a],d=(typeof i)[0];if(o!=d)return"o"==o&&"n"==d||"s"==d||"u"==o;if("o"!=o&&"u"!=o&&n!=i)return n<i;a++}},n=e=>{var r=e[0],t="";if(1===e.length)return"*";if(r+.5){t+=0==r?">=":-1==r?"<":1==r?"^":2==r?"~":r>0?"=":"!=";for(var a=1,o=1;o<e.length;o++)a--,t+="u"==(typeof(d=e[o]))[0]?"-":(a>0?".":"")+(a=2,d);return t}var i=[];for(o=1;o<e.length;o++){var d=e[o];i.push(0===d?"not("+u()+")":1===d?"("+u()+" || "+u()+")":2===d?i.pop()+" "+i.pop():n(d))}return u();function u(){return i.pop().replace(/^\((.+)\)$/,"$1")}},o=(e,r)=>{if(0 in e){r=t(r);var a=e[0],n=a<0;n&&(a=-a-1);for(var i=0,d=1,u=!0;;d++,i++){var l,f,s=d<e.length?(typeof e[d])[0]:"";if(i>=r.length||"o"==(f=(typeof(l=r[i]))[0]))return!u||("u"==s?d>a&&!n:""==s!=n);if("u"==f){if(!u||"u"!=s)return!1}else if(u)if(s==f)if(d<=a){if(l!=e[d])return!1}else{if(n?l>e[d]:l<e[d])return!1;l!=e[d]&&(u=!1)}else if("s"!=s&&"n"!=s){if(n||d<=a)return!1;u=!1,d--}else{if(d<=a||f<s!=n)return!1;u=!1}else"s"!=s&&"n"!=s&&(u=!1,d--)}}var c=[],h=c.pop.bind(c);for(i=1;i<e.length;i++){var p=e[i];c.push(1==p?h()|h():2==p?h()&h():p?o(p,r):!h())}return!!h()},i=(e,r)=>{var t=j.S[e];if(!t||!j.o(t,r))throw new Error("Shared module "+r+" doesn't exist in shared scope "+e);return t},d=(e,r)=>{var t=e[r];return Object.keys(t).reduce(((e,r)=>!e||!t[e].loaded&&a(e,r)?r:e),0)},u=(e,r,t,a)=>"Unsatisfied version "+t+" from "+(t&&e[r][t].from)+" of shared singleton module "+r+" (required "+n(a)+")",l=(e,r,t,a)=>{var n=d(e,t);return o(a,n)||"undefined"!=typeof console&&console.warn&&console.warn(u(e,t,n,a)),s(e[t][n])},f=(e,r,t)=>{var n=e[r];return(r=Object.keys(n).reduce(((e,r)=>!o(t,r)||e&&!a(e,r)?e:r),0))&&n[r]},s=e=>(e.loaded=1,e.get()),h=(c=e=>function(r,t,a,n){var o=j.I(r);return o&&o.then?o.then(e.bind(e,r,j.S[r],t,a,n)):e(r,j.S[r],t,a,n)})(((e,r,t,a)=>(i(e,t),l(r,0,t,a)))),p=c(((e,r,t,a,n)=>{var o=r&&j.o(r,t)&&f(r,t,a);return o?s(o):n()})),v={},b={3725:()=>h("default","@jupyter-widgets/base",[,[1,6,0,0,,"rc",0],[1,4,0,0],[1,3,0,0],[1,2,0,0],[1,1,2,5],1,1,1,1]),7170:()=>h("default","@jupyter-widgets/base",[,[1,6,0,0],[1,5],[1,4],[1,3],[1,2],[1,1],1,1,1,1,1]),3624:()=>p("default","underscore",[1,1,13,1],(()=>j.e(794).then((()=>()=>j(7794))))),9600:()=>p("default","three",[2,0,97,0],(()=>j.e(212).then((()=>()=>j(2212))))),8361:()=>p("default","bluebird",[1,3,5,5],(()=>j.e(624).then((()=>()=>j(6624))))),2473:()=>p("default","jupyter-dataserializers",[1,3,0,0],(()=>Promise.all([j.e(822),j.e(170)]).then((()=>()=>j(6822))))),1526:()=>h("default","@lumino/coreutils",[1,1,11,0])},m={170:[7170],398:[3624,9600,8361,2473,1526],725:[3725]},j.f.consumes=(e,r)=>{j.o(m,e)&&m[e].forEach((e=>{if(j.o(v,e))return r.push(v[e]);var t=r=>{v[e]=0,j.m[e]=t=>{delete j.c[e],t.exports=r()}},a=r=>{delete v[e],j.m[e]=t=>{throw delete j.c[e],r}};try{var n=b[e]();n.then?r.push(v[e]=n.then(t).catch(a)):t(n)}catch(e){a(e)}}))},(()=>{var e={166:0};j.f.j=(r,t)=>{var a=j.o(e,r)?e[r]:void 0;if(0!==a)if(a)t.push(a[2]);else if(/^(170|725)$/.test(r))e[r]=0;else{var n=new Promise(((t,n)=>a=e[r]=[t,n]));t.push(a[2]=n);var o=j.p+j.u(r),i=new Error;j.l(o,(t=>{if(j.o(e,r)&&(0!==(a=e[r])&&(e[r]=void 0),a)){var n=t&&("load"===t.type?"missing":t.type),o=t&&t.target&&t.target.src;i.message="Loading chunk "+r+" failed.\n("+n+": "+o+")",i.name="ChunkLoadError",i.type=n,i.request=o,a[1](i)}}),"chunk-"+r,r)}};var r=(r,t)=>{var a,n,[o,i,d]=t,u=0;if(o.some((r=>0!==e[r]))){for(a in i)j.o(i,a)&&(j.m[a]=i[a]);d&&d(j)}for(r&&r(t);u<o.length;u++)n=o[u],j.o(e,n)&&e[n]&&e[n][0](),e[n]=0},t=self.webpackChunkjupyter_threejs=self.webpackChunkjupyter_threejs||[];t.forEach(r.bind(null,0)),t.push=r.bind(null,t.push.bind(t))})();var w=j(1437);(_JUPYTERLAB=void 0===_JUPYTERLAB?{}:_JUPYTERLAB)["jupyter-threejs"]=w})();