(self.webpackChunkjupyter_webrtc=self.webpackChunkjupyter_webrtc||[]).push([[138,986],{306:e=>{"use strict";e.exports={version:"0.6.0"}},8138:(e,t,i)=>{e.exports=i(1253),e.exports.version=i(306).version},1253:(e,t,i)=>{"use strict";i.r(t),i.d(t,{AudioRecorderModel:()=>k,AudioRecorderView:()=>E,AudioStreamModel:()=>w,AudioStreamView:()=>v,CameraStreamModel:()=>b,ImageRecorderModel:()=>R,ImageRecorderView:()=>M,ImageStreamModel:()=>p,MediaStreamModel:()=>h,MediaStreamView:()=>u,VideoRecorderModel:()=>C,VideoRecorderView:()=>j,VideoStreamModel:()=>g,WebRTCPeerModel:()=>L,WebRTCPeerView:()=>V,WebRTCRoomLocalModel:()=>W,WebRTCRoomModel:()=>x,WebRTCRoomMqttModel:()=>O,WidgetStreamModel:()=>f,WidgetStreamView:()=>y});var s=i(3095),o=i(8731),r=i(2791),a=i(1610);function n(e,t){let i=window.URL.createObjectURL(e);!function(e,t){let i=document.createElement("a");if(i.download=t,i.href=e,document.createEvent){let e=document.createEvent("MouseEvents");e.initMouseEvent("click",!0,!0,window,0,0,0,0,0,!1,!1,!1,!1,0,null),i.dispatchEvent(e)}else lnk.fireEvent&&i.fireEvent("onclick")}(i,t),setTimeout((function(){window.URL.revokeObjectURL(i)}),100)}async function d(e){return new Promise(((t,i)=>{e.readyState>=3?t():e.addEventListener("canplay",t)}))}async function l(e,t){let i,s=e.get("format"),o=e.get("value");if("url"!==s){let t=new Blob([o],{type:`image/${e.get("format")}`});i=URL.createObjectURL(t)}else i=new TextDecoder("utf-8").decode(o.buffer);let r=document.createElement("img");r.src=i;let a=e.get("width");void 0!==a&&a.length>0?r.setAttribute("width",a):r.removeAttribute("width");let n=e.get("height");void 0!==n&&n.length>0?r.setAttribute("height",n):r.removeAttribute("height");let d=t.getContext("2d");return d.drawImage(r,0,0),new Promise(((e,s)=>{r.onload=()=>{t.width=r.width,t.height=r.height,d.drawImage(r,0,0),"string"!=typeof oldurl&&URL.revokeObjectURL(i),e()}}))}i(1171),window.ws=i.g.WebSocket;const c="~"+i(306).version;class h extends s.DOMWidgetModel{defaults(){return{...super.defaults(),_model_module:"jupyter-webrtc",_view_module:"jupyter-webrtc",_model_name:"MediaStreamModel",_view_name:"MediaStreamView",_model_module_version:c,_view_module_version:c}}get stream(){return this.captureStream()}captureStream(){throw new Error("Not implemented")}}const m=function(e){return e.captureStream?e.captureStream():e.stream};class u extends s.DOMWidgetView{render(){super.render.apply(this,arguments),window.last_media_stream_view=this,this.video=document.createElement("video"),this.video.controls=!0,this.pWidget.addClass("jupyter-widgets"),this.pWidget.addClass("widget-image"),this.initPromise=this.model.captureStream(),this.initPromise.then((e=>{this.video.srcObject=e,this.el.appendChild(this.video),this.video.play()}),(e=>{const t=document.createElement("div");t.innerHTML="Error creating view for mediastream: "+e.message,this.el.appendChild(t)}))}remove(){if(null!==this.initPromise)return this.initPromise.then((e=>{this.video.pause(),this.video.srcObject=null})),this.initPromise=null,super.remove.apply(this,arguments)}}class p extends h{defaults(){return{...super.defaults(),_model_name:"ImageStreamModel",image:null}}initialize(){super.initialize.apply(this,arguments),window.last_image_stream=this,this.canvas=document.createElement("canvas"),this.context=this.canvas.getContext("2d"),this.canvas.width=this.get("width"),this.canvas.height=this.get("height"),l(this.get("image"),this.canvas),this.get("image").on("change:value",this.sync_image,this)}sync_image(){if(!this.canvas.captureStream)throw new Error("captureStream not supported for this browser");l(this.get("image"),this.canvas)}async captureStream(){return this.sync_image(),this.canvas.captureStream()}}p.serializers={...h.serializers,image:{deserialize:s.unpack_models}};class _ extends h{defaults(){return{...super.defaults(),playing:!0}}initialize(){super.initialize.apply(this,arguments),this.media=void 0,this.on("change:playing",this.updatePlay,this)}async captureStream(){if(this.createView||(this.createView=o.once((()=>this.widget_manager.create_view(this.get(this.type)).then((e=>{this.media_wid=e,this.media=this.media_wid.el}))))),!this.get(this.type))throw new Error("no media widget passed");if(await this.createView(),!this.media.captureStream&&!this.media.mozCaptureStream)throw new Error("captureStream not supported for this browser");return await d(this.media),this.updatePlay(),this.media.captureStream?this.media.captureStream():this.media.mozCaptureStream?this.media.mozCaptureStream():void 0}updatePlay(){this.get("playing")?this.media.play():this.media.pause()}close(){const e=super.close.apply(this,arguments);return this.media.pause(),this.media_wid.close(),e}}class g extends _{defaults(){return{...super.defaults(),_model_name:"VideoStreamModel",video:null}}initialize(){super.initialize.apply(this,arguments),window.last_video_stream=this,this.type="video"}}g.serializers={..._.serializers,video:{deserialize:s.unpack_models}};class w extends _{defaults(){return{...super.defaults(),_model_name:"AudioStreamModel",_view_name:"AudioStreamView",audio:void 0}}initialize(){super.initialize.apply(this,arguments),window.last_audio_stream=this,this.type="audio"}}w.serializers={..._.serializers,audio:{deserialize:s.unpack_models}};class v extends s.DOMWidgetView{render(){super.render.apply(this,arguments),window.last_audio_stream_view=this,this.audio=document.createElement("audio"),this.audio.controls=!0,this.pWidget.addClass("jupyter-widgets"),this.model.captureStream().then((e=>{this.audio.srcObject=e,this.el.appendChild(this.audio),this.audio.play()}),(e=>{const t=document.createElement("div");t.innerHTML="Error creating view for mediastream: "+e.message,this.el.appendChild(t)}))}remove(){return this.model.captureStream().then((e=>{this.audio.pause(),this.audio.srcObject=null})),s.super.remove.apply(this,arguments)}}class f extends h{defaults(){return{...super.defaults(),_model_name:"WidgetStreamModel",_view_name:"WidgetStreamView",widget:null,max_fps:null,_html2canvas_start_streaming:!1}}initialize(){if(super.initialize.apply(this,arguments),this.on("change:_html2canvas_start_streaming",this.updateHTML2CanvasStreaming,this),this.rendered_view=null,"function"==typeof this.get("widget").captureStream){const e=this.get("max_fps");this.captureStream=()=>null==e?this.get("widget").captureStream():this.get("widget").captureStream(e)}else this.captureStream=()=>{const e=Object.keys(this.get("widget").views);return 0===e.length?new Promise(((e,t)=>{t({message:"Cannot create WidgetStream if the widget has no view rendered"})})):this.get("widget").views[e[0]].then((e=>{this.rendered_view=e;const t=this.find_capturable_obj(this.rendered_view.el);return t?this._captureStream(t):(this.canvas=document.createElement("canvas"),this.set("_html2canvas_start_streaming",!0),this._captureStream(this.canvas))}))}}_captureStream(e){return new Promise(((t,i)=>{const s=this.get("max_fps");e.captureStream&&t(null==s?e.captureStream():e.captureStream(s)),e.mozCaptureStream&&t(null==s?e.mozCaptureStream():e.mozCaptureStream(s)),i(new Error("captureStream not supported for this browser"))}))}find_capturable_obj(e){const t=e.children.length;for(let i=0;i<t;i++){const t=e.children[i];if(t.captureStream||t.mozCaptureStream)return t;const s=this.find_capturable_obj(t);if(s)return s}}updateHTML2CanvasStreaming(){if(this.get("_html2canvas_start_streaming")&&!this.html2CanvasStreaming){let e;this.html2CanvasStreaming=!0;const t=i=>{if(!this._closed){e||(e=i);const s=i-e;e=i;const o=this.get("max_fps");if(0===o);else{let e=0;null!=o&&(e=1e3/o-s,e<0&&(e=0)),setTimeout((()=>{r(this.rendered_view.el,{canvas:this.canvas,logging:!1,useCORS:!0,ignoreElements:e=>!(e.contains(this.rendered_view.el)||this.rendered_view.el.contains(e)||document.head.contains(e))}).then((()=>{window.requestAnimationFrame(t)}))}),e)}}};window.requestAnimationFrame(t)}}}f.serializers={...h.serializers,widget:{deserialize:s.unpack_models}};class y extends u{}class b extends h{defaults(){return{...super.defaults(),_model_name:"CameraStreamModel",constraints:{audio:!0,video:!0}}}captureStream(){return this.cameraStream||(this.cameraStream=navigator.mediaDevices.getUserMedia(this.get("constraints"))),this.cameraStream}close(){return this.cameraStream&&this.cameraStream.then((e=>{e.getTracks().forEach((e=>{e.stop()}))})),super.close.apply(this,arguments)}}class S extends s.DOMWidgetModel{defaults(){return{...super.defaults(),_model_module:"jupyter-webrtc",_view_module:"jupyter-webrtc",_model_module_version:c,_view_module_version:c,stream:null,filename:"record",format:"webm",codecs:"",recording:!1,_data_src:""}}initialize(){super.initialize.apply(this,arguments),this.on("msg:custom",this.handleCustomMessage,this),this.on("change:recording",this.updateRecord,this),this.mediaRecorder=null,this.chunks=[],this.stopping=null}handleCustomMessage(e){"download"===e.msg&&this.download()}get mimeType(){const e=this.get("codecs")||"";let t=`${this.type}/${this.get("format")}`;return e&&(t+=`; codecs="${e}"`),t}updateRecord(){const e=this.get("stream");if(!e)throw new Error("No stream specified");const t=this.mimeType;if(!MediaRecorder.isTypeSupported(t))throw new Error(`The mimeType ${t} is not supported for record on this browser`);this.get("recording")?(this.chunks=[],m(e).then((e=>{this.mediaRecorder=new MediaRecorder(e,{audioBitsPerSecond:128e3,videoBitsPerSecond:25e5,mimeType:t}),this.mediaRecorder.start(),this.mediaRecorder.ondataavailable=e=>{this.chunks.push(e.data)}}))):(this.stopping=new Promise(((e,i)=>{this.mediaRecorder.onstop=i=>{""!==this.get("_data_src")&&URL.revokeObjectURL(this.get("_data_src"));const s=new Blob(this.chunks,{type:t});this.set("_data_src",window.URL.createObjectURL(s)),this.save_changes();const o=new FileReader;o.readAsArrayBuffer(s),o.onloadend=()=>{const t=new Uint8Array(o.result);this.get(this.type).set("value",new DataView(t.buffer)),this.get(this.type).save_changes(),e()}}})),this.stopping.then((()=>{this.stopping=null})),this.mediaRecorder.stop())}download(){if(0===this.chunks.length){if(null===this.stopping)throw new Error("Nothing to download");return void this.stopping.then((()=>{this.download()}))}let e=new Blob(this.chunks,{type:this.mimeType}),t=this.get("filename");t.indexOf(".")<0&&(t=this.get("filename")+"."+this.get("format")),n(e,t)}close(){return""!==this.get("_data_src")&&URL.revokeObjectURL(this.get("_data_src")),super.close.apply(this,arguments)}}S.serializers={...s.DOMWidgetModel.serializers,stream:{deserialize:s.unpack_models}};class z extends s.DOMWidgetView{render(){super.render.apply(this,arguments),this.el.classList.add("jupyter-widgets"),this.buttons=document.createElement("div"),this.buttons.classList.add("widget-inline-hbox"),this.buttons.classList.add("widget-play"),this.recordButton=document.createElement("button"),this.downloadButton=document.createElement("button"),this.result=document.createElement(this.tag),this.result.controls=!0,this.recordButton.className="jupyter-button",this.downloadButton.className="jupyter-button",this.buttons.appendChild(this.recordButton),this.buttons.appendChild(this.downloadButton),this.el.appendChild(this.buttons),this.el.appendChild(this.result);const e=document.createElement("i");e.className=this.recordIconClass,this.recordButton.appendChild(e);const t=document.createElement("i");t.className="fa fa-download",this.downloadButton.appendChild(t),this.recordButton.onclick=()=>{this.model.set("recording",!this.model.get("recording"))},this.downloadButton.onclick=this.model.download.bind(this.model),this.listenTo(this.model,"change:recording",(()=>{this.model.get("recording")?e.style.color="darkred":e.style.color=""})),this.listenTo(this.model,"change:_data_src",(()=>{this.result.src=this.model.get("_data_src"),this.result.play&&this.result.play()}))}}class R extends S{defaults(){return{...super.defaults(),_model_name:"ImageRecorderModel",_view_name:"ImageRecorderView",image:null,_height:"",_width:""}}initialize(){super.initialize.apply(this,arguments),window.last_image_recorder=this,this.type="image"}async snapshot(){const e=this.type+"/"+this.get("format"),t=await m(this.get("stream"));let i=document.createElement("video");i.srcObject=t,i.play(),await d(i),await async function(e){return new Promise(((t,i)=>{e.videoHeight>0?t():e.addEventListener("loadedmetadata",t)}))}(i);let s=document.createElement("canvas"),o=s.getContext("2d"),r=i.videoHeight,a=i.videoWidth;s.height=r,s.width=a,o.drawImage(i,0,0,s.width,s.height);const n=await async function(e,t){return new Promise(((i,s)=>{e.toBlob((e=>i(e)),t)}))}(s,e);this.set("_data_src",window.URL.createObjectURL(n)),this._last_blob=n;const l=await async function(e){return new Promise(((t,i)=>{const s=new FileReader;s.readAsArrayBuffer(e),s.onloadend=()=>{const e=new Uint8Array(s.result);t(e)}}))}(n);this.get(this.type).set("value",new DataView(l.buffer)),this.get(this.type).save_changes(),this.set("_height",r.toString()+"px"),this.set("_width",a.toString()+"px"),this.set("recording",!1),this.save_changes()}updateRecord(){if(!this.get("stream"))throw new Error("No stream specified");""!==this.get("_data_src")&&URL.revokeObjectURL(this.get("_data_src")),this.get("recording")&&this.snapshot()}download(){let e=this.get("filename"),t=this.get("format");e.indexOf(".")<0&&(e=this.get("filename")+"."+t),n(this._last_blob,e)}}R.serializers={...S.serializers,image:{deserialize:s.unpack_models}};class M extends z{initialize(){super.initialize.apply(this,arguments),this.tag="img",this.recordIconClass="fa fa-camera"}}class C extends S{defaults(){return{...super.defaults(),_model_name:"VideoRecorderModel",_view_name:"VideoRecorderView",video:null}}initialize(){super.initialize.apply(this,arguments),window.last_video_recorder=this,this.type="video"}}C.serializers={...S.serializers,video:{deserialize:s.unpack_models}};class j extends z{initialize(){super.initialize.apply(this,arguments),this.tag="video",this.recordIconClass="fa fa-circle"}}class k extends S{defaults(){return{...super.defaults(),_model_name:"AudioRecorderModel",_view_name:"AudioRecorderView",audio:null}}initialize(){super.initialize.apply(this,arguments),window.last_audio_recorder=this,this.type="audio"}}k.serializers={...S.serializers,audio:{deserialize:s.unpack_models}};class E extends z{initialize(){super.initialize.apply(this,arguments),this.tag="audio",this.recordIconClass="fa fa-circle"}}class x extends s.DOMWidgetModel{defaults(){return{...super.defaults(),_model_name:"WebRTCRoomModel",_model_module:"jupyter-webrtc",_model_module_version:c,_view_module_version:c,room:"room",stream:null,room_id:s.uuid(),nickname:"anonymous",peers:[],streams:[]}}log(){let e=[this.get("nickname")+" "+this.get("room_id")+": "];e=e.concat(Array.prototype.slice.call(arguments)),console.log.apply(null,e)}initialize(){super.initialize.apply(this,arguments),this.set("room_id",s.uuid()),this.room_id=this.get("room_id"),this.room=this.get("room"),this.peers={},window["last_webrtc_room_"+this.room_id]=this;const e=this.get("stream");e&&this.set("streams",[e]),this.save_changes(),this.on("msg:custom",this.custom_msg,this)}custom_msg(e){"close"===e.msg&&this.close()}close(){this.get("peers").forEach((e=>e.close()))}create_peer(e){return this.widget_manager.new_widget({model_name:"WebRTCPeerModel",model_module:"jupyter-webrtc",model_module_version:c,view_name:"WebRTCPeerView",view_module:"jupyter-webrtc",view_module_version:c,widget_class:"webrtc.WebRTCPeerModel"},{stream_local:this.get("stream"),id_local:this.get("room_id"),id_remote:e}).then((t=>(t.peer_msg_send=i=>{i.room_id=this.get("room_id"),i.to=e,this.log("send to peer",i),t.save_changes(),this.room_msg_send(i)},t)))}listen_to_remote_stream(e){e.on("change:stream_remote",o.once((()=>{this.log("add remote stream");const t=this.get("streams").slice(),i=e.get("stream_remote");t.push(i),this.set("streams",t),this.save_changes()}))),e.on("change:connected",(()=>{const t=e.get("connected");if(this.log("changed connected status for ",e.get("id_remote"),"to",t),!t){let t=this.get("streams").slice();const i=e.get("stream_remote");t=o.without(t,i),this.set("streams",t);let s=this.get("peers").slice();s=o.without(s,e),this.set("peers",s),delete this.peers[e.get("id_remote")],this.save_changes()}}))}on_room_msg(e){const t=e.room_id;if(e.room_id!==this.room_id)if("join"===e.type)this.log("join from",e.room_id),this.peers[t]=this.create_peer(t).then((e=>(this.listen_to_remote_stream(e),e.join().then((()=>{const t=this.get("peers").slice();t.push(e),this.set("peers",t),this.save_changes()})),e))),this.log(": added peer",t);else if(e.room_id){if(e.to!==this.room_id)return;this.peers[e.room_id]||(this.peers[t]=this.create_peer(t).then((e=>{this.listen_to_remote_stream(e);const t=this.get("peers").slice();return t.push(e),this.set("peers",t),this.save_changes(),e})),this.log("added peer",t));const i=this.peers[e.room_id];i?i.then((t=>{this.log("sending from",e.room_id," to",e.to,e),t.on_peer_msg(e)})):console.error("sending to unknown peer",e.room_id)}else console.error("expected a to room_id to be present")}}x.serializers={...s.DOMWidgetModel.serializers,stream:{deserialize:s.unpack_models},peers:{deserialize:s.unpack_models}};const T={};class W extends x{defaults(){return{...super.defaults(),_model_name:"WebRTCRoomLocalModel"}}initialize(){super.initialize.apply(this,arguments),this.join()}join(){const e=this.get("room");console.log("joining room",e);const t=T[e]||[];t.push((e=>this.on_room_msg(e))),T[e]=t,this.room_msg_send({type:"join",room_id:this.get("room_id")})}room_msg_send(e){const t=this.get("room");console.log("send to room",t,e,T[t]),o.each(T[t],(function(t){t(e)}))}}class O extends x{defaults(){return{...super.defaults(),_model_name:"WebRTCRoomMqttModel",server:"wss://iot.eclipse.org:443/ws"}}initialize(){super.initialize.apply(this,arguments),console.log("connecting to",this.get("server")),this.mqtt_client=a.connect(this.get("server"));const e=this.mqtt_client;this.topic_join="jupyter-webrtc/"+this.get("room")+"/join",this.mqtt_client.on("connect",(()=>{e.subscribe(this.topic_join)})),e.on("message",((e,t)=>{const i=JSON.parse(t);console.log("msg received",t,i),e===this.topic_join&&this.on_room_msg(i)})),this.join()}join(){this.room_msg_send({type:"join",room_id:this.get("room_id")})}room_msg_send(e){const t=JSON.stringify(e);console.log("send to mqtt channel",e),this.mqtt_client.publish(this.topic_join,t)}}class L extends s.DOMWidgetModel{defaults(){return{...super.defaults(),_model_name:"WebRTCPeerModel",_view_name:"WebRTCPeerView",_model_module:"jupyter-webrtc",_view_module:"jupyter-webrtc",_model_module_version:c,_view_module_version:c}}log(){let e=[this.get("room_id")+": "];e=e.concat(Array.prototype.slice.call(arguments)),console.log.apply(null,e)}on_peer_msg(e){if(this.log("peer msg",e),e.sdp){this.log(name,"got sdp");const t=new RTCSessionDescription(e.sdp),i=this.pc.setRemoteDescription(t);this.initiator||(console.log(this.get("id_local"),"did not initiate, reply with answer"),Promise.all([i,this.tracks_added]).then((()=>this.pc.createAnswer())).then((e=>{console.log("sending sdp",this.room_id),this.send_sdp(e),this.pc.setLocalDescription(e)})))}else if(e.candidate){const t=new RTCIceCandidate(e.candidate);this.pc.addIceCandidate(t)}}initialize(){super.initialize.apply(this,arguments);const e=this.room_id=this.get("id_local");this.initiator=!1,this.pc=new RTCPeerConnection({iceServers:[{urls:["stun:stun.l.google.com:19302","stun:stun1.l.google.com:19302","stun:stun2.l.google.com:19302"]}]}),window["last_webrtc_"+e]=this,this.get("stream_local")?this.tracks_added=new Promise(((e,t)=>{this.get("stream_local").stream.then((t=>{console.log("add stream",t),t.getTracks().forEach((e=>{this.pc.addTrack(e,t)})),e()}))})):(console.log("no stream"),this.tracks_added=Promise.resolve()),this.tracks_added.then((()=>console.log("tracks added"))),this.pc.onicecandidate=e=>{console.log(this.room_id,"onicecandidate",e.candidate),this.event_candidate=e,this.send_ice_candidate(e.candidate)},this.pc.onopen=()=>{console.log("onopen",name)},this.pc.onaddstream=e=>{console.log("onaddstream",name),this.widget_manager.new_widget({model_name:"MediaStreamModel",model_module:"jupyter-webrtc",model_module_version:c,view_name:"MediaStreamView",view_module:"jupyter-webrtc",view_module_version:c,widget_class:"webrtc.MediaStreamModel"}).then((t=>(t.captureStream=()=>new Promise(((t,i)=>{t(e.stream)})),this.set("stream_remote",t),this.save_changes(),console.log(this.room_id,": added stream_remote"),t)))},this.pc.onconnecting=()=>{console.log("onconnecting",name)},this.pc.oniceconnectionstatechange=()=>{console.log(this.room_id,"ICE connection state",this.pc.iceConnectionState),"disconnected"===this.pc.iceConnectionState&&(this.set("connected",!1),this.save_changes()),"connected"===this.pc.iceConnectionState&&(this.set("connected",!0),this.save_changes()),"failed"===this.pc.iceConnectionState&&(this.set("connected",!1),this.save_changes())},this.on("msg:custom",this.custom_msg,this),window.addEventListener("beforeunload",(()=>{this.close()}))}custom_msg(e){console.log("custom msg",e),"connect"===e.msg?this.connect():"close"===e.msg?this.close():this.disconnect()}close(){this.pc.close(),this.set("connected",!1),this.save_changes()}join(){return this.initiator=!0,this.tracks_added.then((()=>new Promise(((e,t)=>{const i=this.get("room_id");return this.pc.createOffer({offerToReceiveAudio:1,offerToReceiveVideo:1}).then((t=>{console.log("set local desc"),this.pc.setLocalDescription(t),console.log(i,"send sdp"),this.send_sdp(t),e()})).catch((e=>{console.error(e),t(e)})),this}))))}send_sdp(e){this.broadcast({sdp:e})}send_ice_candidate(e){this.broadcast({candidate:e})}broadcast(e){this.peer_msg_send(e)}}L.serializers={...s.DOMWidgetModel.serializers,stream:{deserialize:s.unpack_models},peers:{deserialize:s.unpack_models}};class V extends s.DOMWidgetView{initialize(){const e=document.createElement("video");window.last_media_view=this,this.setElement(e),super.initialize.apply(this,arguments)}render(){this.model.stream.then((e=>{this.el.srcObject=e,this.el.play()}))}}}}]);