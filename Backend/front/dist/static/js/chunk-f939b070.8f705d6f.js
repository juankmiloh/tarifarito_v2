(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-f939b070"],{"133c":function(t,e,a){"use strict";a("d785")},"3cbc":function(t,e,a){"use strict";var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"pan-item",style:{zIndex:t.zIndex,height:t.height,width:t.width}},[a("div",{staticClass:"pan-info"},[a("div",{staticClass:"pan-info-roles-container"},[t._t("default")],2)]),t._v(" "),a("div",{staticClass:"pan-thumb",style:{backgroundImage:"url("+t.image+")"}})])},n=[],i=(a("c5f6"),{name:"PanThumb",props:{image:{type:String,required:!0},zIndex:{type:Number,default:1},width:{type:String,default:"150px"},height:{type:String,default:"150px"}}}),r=i,c=(a("133c"),a("2877")),o=Object(c["a"])(r,s,n,!1,null,"799537af",null);e["a"]=o.exports},5474:function(t,e,a){"use strict";a("73d2")},"73d2":function(t,e,a){},9406:function(t,e,a){"use strict";a.r(e);var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"dashboard-container"},[a(t.currentRole,{tag:"component"})],1)},n=[],i=(a("6762"),a("2fdb"),a("5530")),r=a("2f62"),c=function(){var t=this,e=t.$createElement,a=t._self._c||e;return t.datosDependencia.nombre?a("div",{staticClass:"div-cont"},[a("el-row",{staticClass:"cont-row"},[a("el-col",{attrs:{span:24}},[a("aside",[a("span",{staticClass:"text-header"},[t._v(t._s(t._f("uppercase")(t.datosDependencia.nombre)))])])]),t._v(" "),a("el-col",{attrs:{span:24}},[a("aside",[a("span",{staticClass:"text-user"},[t._v(t._s(t.privilegio)+" / "+t._s(t.name))])])])],1),t._v(" "),a("el-row",{staticClass:"cont-logo"},[a("el-col",{staticClass:"div-cont-logo",attrs:{sm:24,md:10}},[a("img",{staticClass:"imagePng",attrs:{src:t.logo}})]),t._v(" "),a("el-col",{staticClass:"div-text-logo",attrs:{sm:24,md:14}},[a("el-row",[a("el-col",{attrs:{span:24}},[a("span",{staticClass:"text-superservicios"},[a("b",[t._v("Superservicios")])])]),t._v(" "),a("el-col",{attrs:{span:24}},[a("span",{staticClass:"text-nombre"},[t._v("Superintendencia de Servicios")])]),t._v(" "),a("el-col",{attrs:{span:24}},[a("span",{staticClass:"text-nombre"},[t._v("Públicos Domiciliarios")])])],1)],1)],1)],1):t._e()},o=[],l=(a("96cf"),a("1da1")),d=a("f8ac"),p=a.n(d),u=a("b775");function f(t){return Object(u["a"])({url:"/dependencia",method:"get",params:{iddependencia:t}})}var m={name:"DashboardDefault",components:{},data:function(){return{logo:p.a,datosDependencia:[]}},computed:Object(i["a"])({},Object(r["b"])(["name","avatar","roles","privilegio","dependencia"])),created:function(){this.getInfoDependencia()},methods:{getInfoDependencia:function(){var t=Object(l["a"])(regeneratorRuntime.mark((function t(){var e=this;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,f(this.dependencia).then((function(t){e.datosDependencia=t[0]}));case 2:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}()}},v=m,b=(a("5474"),a("2877")),_=Object(b["a"])(v,c,o,!1,null,"0be95d3a",null),h=_.exports,g=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"dashboard-abogado-container"},[a("el-row",[a("el-col",{staticStyle:{border:"0px solid red","text-align":"center"},attrs:{span:3,xs:24}},[a("pan-thumb",{attrs:{image:t.avatar}},[t._v("\n        Usuario\n        "),a("span",{staticClass:"pan-info-roles"},[t._v(t._s(t.name))])])],1),t._v(" "),a("el-col",{staticClass:"info-container",staticStyle:{border:"0px solid red"},attrs:{span:21,xs:24}},[a("span",{staticClass:"display_name"},[t._v(t._s(t.usuario))]),t._v(" "),a("span",{staticStyle:{"font-size":"20px","padding-top":"20px",display:"inline-block"}},[t._v(t._s(t._f("uppercaseFirst")(t.privilegio)))])]),t._v(" "),a("el-col",{staticClass:"info-container-xs"},[a("el-row",{staticStyle:{"text-align":"center","padding-top":"7%","padding-bottom":"10%"}},[a("el-col",{staticStyle:{"font-size":"xx-large"},attrs:{span:24}},[a("span",[a("b",[t._v(t._s(t.usuario))])])]),t._v(" "),a("el-col",{attrs:{span:24}},[a("span",[t._v(t._s(t._f("uppercaseFirst")(t.privilegio)))])])],1)],1)],1),t._v(" "),a("div",[a("img",{staticClass:"emptyGif",attrs:{src:t.emptyGif}})])],1)},x=[],C=a("3cbc"),w={name:"DashboardAbogado",components:{PanThumb:C["a"]},data:function(){return{emptyGif:"https://wpimg.wallstcn.com/0e03b7da-db9e-4819-ba10-9016ddfdaed3"}},computed:Object(i["a"])({},Object(r["b"])(["name","avatar","roles","usuario","privilegio"]))},y=w,D=(a("f4c5"),Object(b["a"])(y,g,x,!1,null,"46832354",null)),j=D.exports,O={name:"Dashboard",components:{adminDashboard:h,defaultDashboard:j},data:function(){return{currentRole:""}},computed:Object(i["a"])({},Object(r["b"])(["roles"])),created:function(){this.roles.includes("administrador")?this.currentRole="adminDashboard":this.currentRole="defaultDashboard"}},S=O,k=Object(b["a"])(S,s,n,!1,null,null,null);e["default"]=k.exports},d785:function(t,e,a){},e260:function(t,e,a){},f4c5:function(t,e,a){"use strict";a("e260")},f8ac:function(t,e,a){t.exports=a.p+"static/img/superservicios1.1734a3d7.png"}}]);