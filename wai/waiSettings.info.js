(function(){
    var _waiDefaults = function() {

        this.dataServiceDefault = {
            //--------------------------------------------
            // properties - default value setting
            mapUrl      : '',
            serviceUrl  : 'http://127.0.0.1:8080/dataChange_data.xml',
            serviceName : '',
            methodName  : '',
            dsoNames    : '',


            timeOut     : 5000,
            async       : false,
            mapType     : 'xml',
            dataType    : 'xml',
            dsoPublic   : true,

            onErrorThrow : false,
            //--------------------------------------------
            // event callback(s) // do not change value(s)
            onBeforeCall       : null,
            onBeforeCallAttach : null,
            onAfterCallDetach  : null,
            onAfterCall        : null,
            onResultError      : null,
            //--------------------------------------------
            // Etc Options
            fieldNameCaseSen   : 'upper'   // upper = upperCase convert // lower = lowerCase convert // none
        };


        this.downInfo = {
            dynamicServiceDomain : 'http://localhost:8080=ws://127.0.0.1:9892,http://127.0.0.1:8080=wss://127.0.0.1:9893',
            serviceDomain   : 'wss://127.0.0.1:9892',
            webRoots        : '/',
            websocket       : false,
            waiClient       : false,
            waiClient_ie    : '8183',
            waiClient_chrome: '8184',
            waiClient_dft   : '8185',
            dataService     :  window.location.protocol + "//" + window.location.hostname + "" + ':8090/JSONDataService',
            async           : true,
            timeOut         : 10000,
            serviceLog      : false
        };

        this.clientServiceDefault = {
            port        : 9515
        };

        this.dateFormat    = 'ddmmyyyy';
        this.dateSeparator = '/';
        this.getDateFormat = ''; //dd-mm-yyyy
        this.urlPrefix = '';
        this.grid_SplashText = '<No data to display>'; //<No data to display>
        this.arbitrary_precision = true; //arbitrary-precision arithmetic.

        this.dateLang = 'english'; // korean, chinese, indonesia
        this.dateLangData = {
            'english' : {
                weeks: ['S', 'M', 'T', 'W', 'T', 'F', 'S'],
                months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            },
            'korean' : {
                weeks: ['일', '월', '화', '수', '목', '금', '토'],
                months: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']
            },
            'chinese' : {
                weeks: ['日', '月', '火', '水', '木', '金', '土'],
                months: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
            },
            'indonesia' : {
                weeks: ['M', 'S', 'S', 'R', 'K', 'J', 'S'],
                months: ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']
            }
        };

        this.editorFontList = [
            {name: "굴림",              value: "Gulim"},
            {name: "굴림체",            value: "GulimChe"},
            {name: "궁서",              value: "Gungsuh"},
            {name: "궁서체",            value: "GungsuhChe"},
            {name: "나눔고딕",          value: "NanumGothic"},
            {name: "돋움",              value: "Dotum"},
            {name: "돋움체",            value: "DotumChe"},
            {name: "맑은 고딕",         value: "Malgun Gothic"},
            {name: "바탕",              value: "Batang"},
            {name: "바탕체",            value: "BatangChe"},
            {name: "새굴림",            value: "New Gulim"},
            {name: "Arial",             value: "Arial"},
            {name: "Arial Black",       value: "Arial Black"},
            {name: "Arial Narrow",      value: "Arial Narrow"},
            {name: "Bookman Old Style", value: "Bookman Old Style"},
            {name: "Century",           value: "Century"},
            {name: "Century Gothic",    value: "Century Gothic"},
            {name: "Comic Sans MS",     value: "Comic Sans MS"},
            {name: "Courier New",       value: "Courier New"},
            {name: "Cursive",           value: "Cursive"},
            {name: "fantasy",           value: "fantasy"},
            {name: "Garamond",          value: "Garamond"},
            {name: "Georgia",           value: "Georgia"},
            {name: "impact",            value: "impact"},
            {name: "Lucida Console",    value: "Lucida Console"},
            {name: "monospace",         value: "monospace"},
            {name: "MS Gothic",         value: "MS Gothic"},
            {name: "MS PGothic",        value: "MS PGothic"},
            {name: "MS Sans Serif",     value: "MS Sans Serif"},
            {name: "MS Serif",          value: "MS Serif"},
            {name: "sans-serif",        value: "sans-serif"},
            {name: "SimSun",            value: "SimSun"},
            {name: "Tahoma",            value: "Tahoma"},
            {name: "Times New Roman",   value: "Times New Roman"},
            {name: "Verdana",           value: "Verdana"}
        ];

        this.SerialNumber  = "524139A916F655B6E35C295F70D4E9BC";
    };

    $wai.default = new _waiDefaults();
})();
// END of file