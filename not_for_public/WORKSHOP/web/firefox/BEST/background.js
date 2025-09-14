function openTab() {
  // body... 	
  browser.tabs.create({
    url: browser.runtime.getURL("index.html")
  });
  browser.tabs.create({
    url: "https://www.google.com"
  });
  // itemLoad();
}
// function itemLoad() {
//     document.getElementById("bookmark_pane") = 

// }
browser.browserAction.onClicked.addListener(openTab);
    //     function makeIndent(indentLength) {
    //         return ".".repeat(indentLength);
    //     }

    //     function logItems(bookmarkItem, indent) {
    //         if (bookmarkItem.url) {
    //             console.log(makeIndent(indent) + bookmarkItem.url);
    //         } else {
    //             console.log(makeIndent(indent) + "Folder");
    //             indent++;
    //         }
    //         if (bookmarkItem.children) {
    //             for (child of bookmarkItem.children) {
    //                 logItems(child, indent);
    //             }
    //         }
    //         indent--;
    //     }

    //     function logTree(bookmarkItems) {
    //         logItems(bookmarkItems[0], 0);
    //     }

    //     function onRejected(error) {
    //         console.log(`An error: ${error}`);
    //     }

    //     var gettingTree = browser.bookmarks.getTree();
    //     gettingTree.then(logTree, onRejected);




// tested functionalities but not used
// function openNewWindow () {
// 	// body... 
// 	browser.windows.create({
// 		url: "https://mozilla.org"
// 	});
// }
// browser.browserAction.onClicked.addListener(openNewWindow);

// This page is loaded from an extention