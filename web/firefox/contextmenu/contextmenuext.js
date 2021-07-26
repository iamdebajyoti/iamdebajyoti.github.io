//creating the context menu / right-click menu

browser.contextMenus.create({
    id: "ext1",
    title: "new right click menu",
    contexts: ["all"]

});

browser.contextMenus.onClicked.addListener(contextMenuAction);

function contextMenuAction(info, tab) {
    // body... 
    const msg = "You have selected" + info.selectionText;
    // browser.tabs.sendMessage(tab.id, { msg });
    alert(msg);
}