var _JUPYTERLAB;(()=>{"use strict";var e,r,t,a,n,o,d,i,c,l,u,f,s,h,p,b,v,m,y={7449:(e,r,t)=>{var a={"./index":()=>t.e(568).then((()=>()=>t(1568))),"./extension":()=>Promise.all([t.e(568),t.e(261)]).then((()=>()=>t(6261)))},n=(e,r)=>(t.R=r,r=t.o(a,e)?a[e]():Promise.resolve().then((()=>{throw new Error('Module "'+e+'" does not exist in container.')})),t.R=void 0,r),o=(e,r)=>{if(t.S){var a=t.S.default,n="default";if(a&&a!==e)throw new Error("Container initialization failed as it has already been initialized with a different share scope");return t.S[n]=e,t.I(n,r)}};t.d(r,{get:()=>n,init:()=>o})}},g={};function w(e){var r=g[e];if(void 0!==r)return r.exports;var t=g[e]={id:e,loaded:!1,exports:{}};return y[e].call(t.exports,t,t.exports,w),t.loaded=!0,t.exports}w.m=y,w.c=g,w.d=(e,r)=>{for(var t in r)w.o(r,t)&&!w.o(e,t)&&Object.defineProperty(e,t,{enumerable:!0,get:r[t]})},w.f={},w.e=e=>Promise.all(Object.keys(w.f).reduce(((r,t)=>(w.f[t](e,r),r)),[])),w.u=e=>e+"."+{58:"5dd767d4301576cee659",64:"e6b27f39dcb5e033dca2",212:"b0149a14735c9b14c049",261:"a9c9630b28934bcbf1c3",466:"df53a5241872f78b6b60",486:"59ac5542d87a8f7709e9",501:"54c2baeab80ecb56ca08",568:"df354347cf6898d012c4",577:"ef610ec4539ffe9cddc1",861:"845bccd8cacebe4b0886",936:"34edf02ccabe0274c00d",943:"4d08ec41a49be026ca9f"}[e]+".js?v="+{58:"5dd767d4301576cee659",64:"e6b27f39dcb5e033dca2",212:"b0149a14735c9b14c049",261:"a9c9630b28934bcbf1c3",466:"df53a5241872f78b6b60",486:"59ac5542d87a8f7709e9",501:"54c2baeab80ecb56ca08",568:"df354347cf6898d012c4",577:"ef610ec4539ffe9cddc1",861:"845bccd8cacebe4b0886",936:"34edf02ccabe0274c00d",943:"4d08ec41a49be026ca9f"}[e],w.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),w.o=(e,r)=>Object.prototype.hasOwnProperty.call(e,r),e={},r="ipyvolume:",w.l=(t,a,n,o)=>{if(e[t])e[t].push(a);else{var d,i;if(void 0!==n)for(var c=document.getElementsByTagName("script"),l=0;l<c.length;l++){var u=c[l];if(u.getAttribute("src")==t||u.getAttribute("data-webpack")==r+n){d=u;break}}d||(i=!0,(d=document.createElement("script")).charset="utf-8",d.timeout=120,w.nc&&d.setAttribute("nonce",w.nc),d.setAttribute("data-webpack",r+n),d.src=t),e[t]=[a];var f=(r,a)=>{d.onerror=d.onload=null,clearTimeout(s);var n=e[t];if(delete e[t],d.parentNode&&d.parentNode.removeChild(d),n&&n.forEach((e=>e(a))),r)return r(a)},s=setTimeout(f.bind(null,void 0,{type:"timeout",target:d}),12e4);d.onerror=f.bind(null,d.onerror),d.onload=f.bind(null,d.onload),i&&document.head.appendChild(d)}},w.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},w.nmd=e=>(e.paths=[],e.children||(e.children=[]),e),(()=>{w.S={};var e={},r={};w.I=(t,a)=>{a||(a=[]);var n=r[t];if(n||(n=r[t]={}),!(a.indexOf(n)>=0)){if(a.push(n),e[t])return e[t];w.o(w.S,t)||(w.S[t]={});var o=w.S[t],d="ipyvolume",i=(e,r,t,a)=>{var n=o[e]=o[e]||{},i=n[r];(!i||!i.loaded&&(!a!=!i.eager?a:d>i.from))&&(n[r]={get:t,from:d,eager:!!a})},c=[];switch(t){case"default":i("d3","5.12.0",(()=>w.e(64).then((()=>()=>w(64))))),i("ipyvolume","0.6.3",(()=>w.e(568).then((()=>()=>w(1568))))),i("is-typedarray","1.0.0",(()=>w.e(501).then((()=>()=>w(4501))))),i("lodash","4.17.15",(()=>w.e(486).then((()=>()=>w(6486))))),i("mustache","2.3.2",(()=>w.e(466).then((()=>()=>w(466))))),i("ndarray-pack","1.2.1",(()=>Promise.all([w.e(943),w.e(936)]).then((()=>()=>w(1943))))),i("ndarray","1.0.18",(()=>w.e(861).then((()=>()=>w(2861))))),i("screenfull","3.3.3",(()=>w.e(577).then((()=>()=>w(577))))),i("three-text2d","0.4.1",(()=>w.e(58).then((()=>()=>w(5058))))),i("three","0.97.0",(()=>w.e(212).then((()=>()=>w(2212)))))}return e[t]=c.length?Promise.all(c).then((()=>e[t]=1)):1}}})(),(()=>{var e;w.g.importScripts&&(e=w.g.location+"");var r=w.g.document;if(!e&&r&&(r.currentScript&&(e=r.currentScript.src),!e)){var t=r.getElementsByTagName("script");t.length&&(e=t[t.length-1].src)}if(!e)throw new Error("Automatic publicPath is not supported in this browser");e=e.replace(/#.*$/,"").replace(/\?.*$/,"").replace(/\/[^\/]+$/,"/"),w.p=e})(),t=e=>{var r=e=>e.split(".").map((e=>+e==e?+e:e)),t=/^([^-+]+)?(?:-([^+]+))?(?:\+(.+))?$/.exec(e),a=t[1]?r(t[1]):[];return t[2]&&(a.length++,a.push.apply(a,r(t[2]))),t[3]&&(a.push([]),a.push.apply(a,r(t[3]))),a},a=(e,r)=>{e=t(e),r=t(r);for(var a=0;;){if(a>=e.length)return a<r.length&&"u"!=(typeof r[a])[0];var n=e[a],o=(typeof n)[0];if(a>=r.length)return"u"==o;var d=r[a],i=(typeof d)[0];if(o!=i)return"o"==o&&"n"==i||"s"==i||"u"==o;if("o"!=o&&"u"!=o&&n!=d)return n<d;a++}},n=e=>{var r=e[0],t="";if(1===e.length)return"*";if(r+.5){t+=0==r?">=":-1==r?"<":1==r?"^":2==r?"~":r>0?"=":"!=";for(var a=1,o=1;o<e.length;o++)a--,t+="u"==(typeof(i=e[o]))[0]?"-":(a>0?".":"")+(a=2,i);return t}var d=[];for(o=1;o<e.length;o++){var i=e[o];d.push(0===i?"not("+c()+")":1===i?"("+c()+" || "+c()+")":2===i?d.pop()+" "+d.pop():n(i))}return c();function c(){return d.pop().replace(/^\((.+)\)$/,"$1")}},o=(e,r)=>{if(0 in e){r=t(r);var a=e[0],n=a<0;n&&(a=-a-1);for(var d=0,i=1,c=!0;;i++,d++){var l,u,f=i<e.length?(typeof e[i])[0]:"";if(d>=r.length||"o"==(u=(typeof(l=r[d]))[0]))return!c||("u"==f?i>a&&!n:""==f!=n);if("u"==u){if(!c||"u"!=f)return!1}else if(c)if(f==u)if(i<=a){if(l!=e[i])return!1}else{if(n?l>e[i]:l<e[i])return!1;l!=e[i]&&(c=!1)}else if("s"!=f&&"n"!=f){if(n||i<=a)return!1;c=!1,i--}else{if(i<=a||u<f!=n)return!1;c=!1}else"s"!=f&&"n"!=f&&(c=!1,i--)}}var s=[],h=s.pop.bind(s);for(d=1;d<e.length;d++){var p=e[d];s.push(1==p?h()|h():2==p?h()&h():p?o(p,r):!h())}return!!h()},d=(e,r)=>{var t=w.S[e];if(!t||!w.o(t,r))throw new Error("Shared module "+r+" doesn't exist in shared scope "+e);return t},i=(e,r)=>{var t=e[r];return Object.keys(t).reduce(((e,r)=>!e||!t[e].loaded&&a(e,r)?r:e),0)},c=(e,r,t)=>"Unsatisfied version "+r+" of shared singleton module "+e+" (required "+n(t)+")",l=(e,r,t,a)=>{var n=i(e,t);return o(a,n)||"undefined"!=typeof console&&console.warn&&console.warn(c(t,n,a)),f(e[t][n])},u=(e,r,t)=>{var n=e[r];return(r=Object.keys(n).reduce(((e,r)=>!o(t,r)||e&&!a(e,r)?e:r),0))&&n[r]},f=e=>(e.loaded=1,e.get()),h=(s=e=>function(r,t,a,n){var o=w.I(r);return o&&o.then?o.then(e.bind(e,r,w.S[r],t,a,n)):e(r,w.S[r],t,a,n)})(((e,r,t,a)=>(d(e,t),l(r,0,t,a)))),p=s(((e,r,t,a,n)=>{var o=r&&w.o(r,t)&&u(r,t,a);return o?f(o):n()})),b={},v={366:()=>p("default","d3",[1,5,7,0],(()=>w.e(64).then((()=>()=>w(64))))),687:()=>p("default","mustache",[1,2,3,1],(()=>w.e(466).then((()=>()=>w(466))))),1228:()=>p("default","three-text2d",[2,0,4,1],(()=>w.e(58).then((()=>()=>w(5058))))),1251:()=>p("default","ndarray-pack",[1,1,2,1],(()=>Promise.all([w.e(943),w.e(936)]).then((()=>()=>w(1943))))),2461:()=>h("default","@jupyter-widgets/base",[,[1,6],[1,5],[1,4],[1,3],[1,2,0,2],[1,1],1,1,1,1,1]),4600:()=>p("default","is-typedarray",[2,1,0,0],(()=>w.e(501).then((()=>()=>w(4501))))),5995:()=>p("default","ndarray",[2,1,0,18],(()=>w.e(861).then((()=>()=>w(2861))))),8174:()=>p("default","lodash",[1,4,17,15],(()=>w.e(486).then((()=>()=>w(6486))))),8299:()=>p("default","screenfull",[1,3,3,1],(()=>w.e(577).then((()=>()=>w(577))))),9600:()=>p("default","three",[2,0,97,0],(()=>w.e(212).then((()=>()=>w(2212))))),3936:()=>p("default","ndarray",[1,1,0,13],(()=>w.e(861).then((()=>()=>w(2861))))),1153:()=>p("default","three",[0],(()=>w.e(212).then((()=>()=>w(2212)))))},m={58:[1153],568:[366,687,1228,1251,2461,4600,5995,8174,8299,9600],936:[3936]},w.f.consumes=(e,r)=>{w.o(m,e)&&m[e].forEach((e=>{if(w.o(b,e))return r.push(b[e]);var t=r=>{b[e]=0,w.m[e]=t=>{delete w.c[e],t.exports=r()}},a=r=>{delete b[e],w.m[e]=t=>{throw delete w.c[e],r}};try{var n=v[e]();n.then?r.push(b[e]=n.then(t).catch(a)):t(n)}catch(e){a(e)}}))},(()=>{var e={357:0};w.f.j=(r,t)=>{var a=w.o(e,r)?e[r]:void 0;if(0!==a)if(a)t.push(a[2]);else if(936!=r){var n=new Promise(((t,n)=>a=e[r]=[t,n]));t.push(a[2]=n);var o=w.p+w.u(r),d=new Error;w.l(o,(t=>{if(w.o(e,r)&&(0!==(a=e[r])&&(e[r]=void 0),a)){var n=t&&("load"===t.type?"missing":t.type),o=t&&t.target&&t.target.src;d.message="Loading chunk "+r+" failed.\n("+n+": "+o+")",d.name="ChunkLoadError",d.type=n,d.request=o,a[1](d)}}),"chunk-"+r,r)}else e[r]=0};var r=(r,t)=>{var a,n,[o,d,i]=t,c=0;for(a in d)w.o(d,a)&&(w.m[a]=d[a]);for(i&&i(w),r&&r(t);c<o.length;c++)n=o[c],w.o(e,n)&&e[n]&&e[n][0](),e[o[c]]=0},t=self.webpackChunkipyvolume=self.webpackChunkipyvolume||[];t.forEach(r.bind(null,0)),t.push=r.bind(null,t.push.bind(t))})();var S=w(7449);(_JUPYTERLAB=void 0===_JUPYTERLAB?{}:_JUPYTERLAB).ipyvolume=S})();