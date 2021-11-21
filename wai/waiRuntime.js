/**
 *  [ wai ] Loader
 *
 *  Copyright(C) 2017 Corebank Co.,Ltd. All rights reserved.
 */
var $waiIntegrated = true;
(function(){
    var rootUrl = '/wai';
    var loadFiles = [];

    if($waiIntegrated){
        loadFiles = [
            {
                'url'   :'/waiAll.css',
                'cache': true
            },
            {
                'url'   :'/waiAll.js',
                'cache': true
            },
            {
                'url'   :'/waiSettings.info.js',
                'cache': true
            },
            {
                'url'   :'/lib/waiRTL.min.js',
                'cache': true
            }
        ];
    }else{
        loadFiles = [
            {
                'url'   :'/Y[wai]/wai.js',
                'cache': true
            }
        ];
    }
    document.write("<!--wai.loader.start-->");

    var dt = new Date();
    var ca = '';

    for (var i=0;i<loadFiles.length;i++){
        ca = loadFiles[i].cache ? '' : '?nocache='+dt.toString();
        var ext = getExtensionOfFilename(loadFiles[i].url);

        if(ext == ".js") {
            document.write('<script type="text/javascript" src="' + rootUrl + loadFiles[i].url + ca + '"></script>');
        }
        else if(ext == ".css") {
            document.write('<link rel="stylesheet" type="text/css" href="' + rootUrl + loadFiles[i].url + ca + '">');
        }
    }

    document.write("<!--wai.loader.end-->");

    function getExtensionOfFilename(filename) {

        var _fileLen = filename.length;

        /**
         * lastIndexOf('.')
         * 뒤에서부터 '.'의 위치를 찾기위한 함수
         * 검색 문자의 위치를 반환한다.
         * 파일 이름에 '.'이 포함되는 경우가 있기 때문에 lastIndexOf() 사용
         */
        var _lastDot = filename.lastIndexOf('.');

        // 확장자 명만 추출한 후 소문자로 변경
        var _fileExt = filename.substring(_lastDot, _fileLen).toLowerCase();

        return _fileExt;
    }
})();
