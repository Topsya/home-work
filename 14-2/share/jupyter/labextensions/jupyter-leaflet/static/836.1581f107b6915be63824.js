"use strict";(self.webpackChunkjupyter_leaflet=self.webpackChunkjupyter_leaflet||[]).push([[836],{9836:(t,n,e)=>{e.r(n);var i=e(2081);function o(t,n){var e=i.DomUtil.create("div",t,document.body),o=function(t){var n=a(t,"background-image");return n&&"none"!==n?n:a(t,"cursor")}(e),r=function(t,n){for(var e,i=/url\(['"]?([^"']*?)['"]?\)/gi,o=[],r=i.exec(t);r;)o.push(n?(e=r[1]).substr(e.lastIndexOf("/")+1):r[1]),r=i.exec(t);return o}(o,n),s=l(e,"width"),u=l(e,"height"),c=l(e,"margin-left"),p=l(e,"margin-top");return e.parentNode.removeChild(e),{Url:r[0],RetinaUrl:r[1],Size:[s,u],Anchor:[-c,-p]}}function r(t){var n=i.DomUtil.create("div",t,document.body),e=l(n,"margin-left"),o=l(n,"margin-top");return n.parentNode.removeChild(n),{Anchor:[e,o]}}function l(t,n){return parseInt(a(t,n),10)}function a(t,n){return i.DomUtil.getStyle(t,n)||i.DomUtil.getStyle(t,n.replace(/-(\w)/g,(function(t,n){return n.toUpperCase()})))}i.Icon.Default.mergeOptions({iconUrl:null,iconRetinaUrl:null,shadowUrl:null,iconSize:null,iconAnchor:null,popupAnchor:null,tooltipAnchor:null,shadowSize:null,classNamePrefix:"leaflet-default-icon-"}),i.Icon.Default.include({_needsInit:!0,_getIconUrl:function(t){var n=this.options.imagePath||i.Icon.Default.imagePath||"";return this._needsInit&&this._initializeOptions(n),n+i.Icon.prototype._getIconUrl.call(this,t)},_initializeOptions:function(t){this._setOptions("icon",o,t),this._setOptions("shadow",o,t),this._setOptions("popup",r),this._setOptions("tooltip",r),this._needsInit=!1},_setOptions:function(t,n,e){var i=this.options,o=n(i.classNamePrefix+t,e);for(var r in o)i[t+r]=i[t+r]||o[r]}})}}]);