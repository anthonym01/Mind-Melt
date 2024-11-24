ace.define("ace/mode/ion_highlight_rules",["require","exports","module","ace/lib/oop","ace/mode/text_highlight_rules"], function(require, exports, module) {
    "use strict";

    var oop = require("../lib/oop");
    var TextHighlightRules = require("./text_highlight_rules").TextHighlightRules;


    var IonHighlightRules = function() {
        var k_keywords_bool =
            "TRUE|FALSE";
        var k_bool = k_keywords_bool;
        var k_keywords_null =
            "NULL.NULL|NULL.BOOL|NULL.INT|NULL.FLOAT|NULL.DECIMAL|NULL.TIMESTAMP|NULL.STRING|NULL.SYMBOL|NULL.BLOB|NULL.CLOB|"
            +"NULL.STRUCT|NULL.LIST|NULL.SEXP|NULL";
        var k_null = k_keywords_null;


        var keywordMapper = this.createKeywordMapper({
            "constant.language.bool.ion": k_bool,
            "constant.language.null.ion": k_null
        }, "constant.other.symbol.identifier.ion", true);

        var keywordMapperRule = {
            token : keywordMapper,
            regex : "\\b\\w+(?:\\.\\w+)?\\b"
        };

        this.$rules = {
          "start": [
            {
              "include": "value"
            }
          ],
          "value": [
            {
              "include": "whitespace"
            },
            {
              "include": "comment"
            },
            {
              "include": "annotation"
            },
            {
              "include": "string"
            },
            {
              "include": "number"
            },
            {
              "include": "keywords"
            },
            {
              "include": "symbol"
            },
            {
              "include": "clob"
            },
            {
              "include": "blob"
            },
            {
              "include": "struct"
            },
            {
              "include": "list"
            },
            {
              "include": "sexp"
            }
          ],
          "sexp": [
            {
              "token": "punctuation.definition.sexp.begin.ion",
              "regex": "\\(",
              "push": [
                {
                  "token": "punctuation.definition.sexp.end.ion",
                  "regex": "\\)",
                  "next": "pop"
                },
                {
                  "include": "comment"
                },
                {
                  "include": "value"
                },
                {
                  "token": "punctuation.definition.symbol.operator.ion",
                  "regex": "[\\!\\#\\%\\&\\*\\+\\-\\./\\;\\<\\=\\>\\?\\@\\^\\`\\|\\~]"
                }
              ]
            }
          ],
          "comment": [
            {
              "token": "comment.line.ion",
              "regex": "//[^\\n]*"
            },
            {
              "token": "comment.block.ion",
              "regex": "/\\*",
              "push": [
                {
                  "token": "comment.block.ion",
                  "regex": "\\*/",
                  "next": "pop"
                },
                {
                  "token": "comment.block.ion",
                  "regex": "(:?.|[^\\*]+)"
                }
              ]
            }
          ],
          "list": [
            {
              "token": "punctuation.definition.list.begin.ion",
              "regex": "\\[",
              "push": [
                {
                  "token": "punctuation.definition.list.end.ion",
                  "regex": "\\]",
                  "next": "pop"
                },
                {
                  "include": "comment"
                },
                {
                  "include": "value"
                },
                {
                  "token": "punctuation.definition.list.separator.ion",
                  "regex": ","
                }
              ]
            }
          ],
          "struct": [
            {
              "token": "punctuation.definition.struct.begin.ion",
              "regex": "\\{",
              "push": [
                {
                  "token": "punctuation.definition.struct.end.ion",
                  "regex": "\\}",
                  "next": "pop"
                },
                {
                  "include": "comment"
                },
                {
                  "include": "value"
                },
                {
                  "token": "punctuation.definition.struct.separator.ion",
                  "regex": ",|:"
                }
              ]
            }
          ],
          "blob": [
            {
              "token": [
                "punctuation.definition.blob.begin.ion",
                "string.other.blob.ion",
                "punctuation.definition.blob.end.ion"
              ],
              "regex": "(\\{\\{)([^\"]*)(\\}\\})"
            }
          ],
          "clob": [
            {
              "token": [
                "punctuation.definition.clob.begin.ion",
                "string.other.clob.ion",
                "punctuation.definition.clob.end.ion"
              ],
              "regex": "(\\{\\{)(\"[^\"]*\")(\\}\\})"
            }
          ],
          "symbol": [
            {
              "token": "constant.other.symbol.quoted.ion",
              "regex": "(['])((?:(?:\\\\')|(?:[^']))*?)(['])"
            },
            {
              "token": "constant.other.symbol.identifier.ion",
              "regex": "[\\$_a-zA-Z][\\$_a-zA-Z0-9]*"
            }
          ],
          "number": [
            {
              "token": "constant.numeric.timestamp.ion",
              "regex": "\\d{4}(?:-\\d{2})?(?:-\\d{2})?T(?:\\d{2}:\\d{2})(?::\\d{2})?(?:\\.\\d+)?(?:Z|[-+]\\d{2}:\\d{2})?"
            },
            {
              "token": "constant.numeric.timestamp.ion",
              "regex": "\\d{4}-\\d{2}-\\d{2}T?"
            },
            {
              "token": "constant.numeric.integer.binary.ion",
              "regex": "-?0[bB][01](?:_?[01])*"
            },
            {
              "token": "constant.numeric.integer.hex.ion",
              "regex": "-?0[xX][0-9a-fA-F](?:_?[0-9a-fA-F])*"
            },
            {
              "token": "constant.numeric.float.ion",
              "regex": "-?(?:0|[1-9](?:_?\\d)*)(?:\\.(?:\\d(?:_?\\d)*)?)?(?:[eE][+-]?\\d+)"
            },
            {
              "token": "constant.numeric.float.ion",
              "regex": "(?:[-+]inf)|(?:nan)"
            },
            {
              "token": "constant.numeric.decimal.ion",
              "regex": "-?(?:0|[1-9](?:_?\\d)*)(?:(?:(?:\\.(?:\\d(?:_?\\d)*)?)(?:[dD][+-]?\\d+)|\\.(?:\\d(?:_?\\d)*)?)|(?:[dD][+-]?\\d+))"
            },
            {
              "token": "constant.numeric.integer.ion",
              "regex": "-?(?:0|[1-9](?:_?\\d)*)"
            }
          ],
          "string": [
            {
              "token": [
                "punctuation.definition.string.begin.ion",
                "string.quoted.double.ion",
                "punctuation.definition.string.end.ion"
              ],
              "regex": "([\"])((?:(?:\\\\\")|(?:[^\"]))*?)([\"])"
            },
            {
              "token": "punctuation.definition.string.begin.ion",
              "regex": "'{3}",
              "push": [
                {
                  "token": "punctuation.definition.string.end.ion",
                  "regex": "'{3}",
                  "next": "pop"
                },
                {
                  "token": "string.quoted.triple.ion",
                  "regex": "(?:\\\\'*|.|[^']+)"
                }
              ]
            }
          ],
          "annotation": [
            {
              "token": "variable.language.annotation.ion",
              "regex": "'(?:[^']|\\\\\\\\|\\\\')*'\\s*::"
            },
            {
              "token": "variable.language.annotation.ion",
              "regex": "[\\$_a-zA-Z][\\$_a-zA-Z0-9]*::"
            }
          ],
          "whitespace": [
            {
              "token": "text.ion",
              "regex": "\\s+"
            }
          ]
        } ;
        this.$rules["keywords"] = [keywordMapperRule];


        this.normalizeRules();
    };

    oop.inherits(IonHighlightRules, TextHighlightRules);

    exports.IonHighlightRules = IonHighlightRules;
});

ace.define("ace/mode/matching_brace_outdent",["require","exports","module","ace/range"], function(require, exports, module) {
"use strict";

var Range = require("../range").Range;

var MatchingBraceOutdent = function() {};

(function() {

    this.checkOutdent = function(line, input) {
        if (! /^\s+$/.test(line))
            return false;

        return /^\s*\}/.test(input);
    };

    this.autoOutdent = function(doc, row) {
        var line = doc.getLine(row);
        var match = line.match(/^(\s*\})/);

        if (!match) return 0;

        var column = match[1].length;
        var openBracePos = doc.findMatchingBracket({row: row, column: column});

        if (!openBracePos || openBracePos.row == row) return 0;

        var indent = this.$getIndent(doc.getLine(openBracePos.row));
        doc.replace(new Range(row, 0, row, column-1), indent);
    };

    this.$getIndent = function(line) {
        return line.match(/^\s*/)[0];
    };

}).call(MatchingBraceOutdent.prototype);

exports.MatchingBraceOutdent = MatchingBraceOutdent;
});

ace.define("ace/mode/folding/cstyle",["require","exports","module","ace/lib/oop","ace/range","ace/mode/folding/fold_mode"], function(require, exports, module) {
"use strict";

var oop = require("../../lib/oop");
var Range = require("../../range").Range;
var BaseFoldMode = require("./fold_mode").FoldMode;

var FoldMode = exports.FoldMode = function(commentRegex) {
    if (commentRegex) {
        this.foldingStartMarker = new RegExp(
            this.foldingStartMarker.source.replace(/\|[^|]*?$/, "|" + commentRegex.start)
        );
        this.foldingStopMarker = new RegExp(
            this.foldingStopMarker.source.replace(/\|[^|]*?$/, "|" + commentRegex.end)
        );
    }
};
oop.inherits(FoldMode, BaseFoldMode);

(function() {
    
    this.foldingStartMarker = /([\{\[\(])[^\}\]\)]*$|^\s*(\/\*)/;
    this.foldingStopMarker = /^[^\[\{\(]*([\}\]\)])|^[\s\*]*(\*\/)/;
    this.singleLineBlockCommentRe= /^\s*(\/\*).*\*\/\s*$/;
    this.tripleStarBlockCommentRe = /^\s*(\/\*\*\*).*\*\/\s*$/;
    this.startRegionRe = /^\s*(\/\*|\/\/)#?region\b/;
    this._getFoldWidgetBase = this.getFoldWidget;
    this.getFoldWidget = function(session, foldStyle, row) {
        var line = session.getLine(row);
    
        if (this.singleLineBlockCommentRe.test(line)) {
            if (!this.startRegionRe.test(line) && !this.tripleStarBlockCommentRe.test(line))
                return "";
        }
    
        var fw = this._getFoldWidgetBase(session, foldStyle, row);
    
        if (!fw && this.startRegionRe.test(line))
            return "start"; // lineCommentRegionStart
    
        return fw;
    };

    this.getFoldWidgetRange = function(session, foldStyle, row, forceMultiline) {
        var line = session.getLine(row);
        
        if (this.startRegionRe.test(line))
            return this.getCommentRegionBlock(session, line, row);
        
        var match = line.match(this.foldingStartMarker);
        if (match) {
            var i = match.index;

            if (match[1])
                return this.openingBracketBlock(session, match[1], row, i);
                
            var range = session.getCommentFoldRange(row, i + match[0].length, 1);
            
            if (range && !range.isMultiLine()) {
                if (forceMultiline) {
                    range = this.getSectionRange(session, row);
                } else if (foldStyle != "all")
                    range = null;
            }
            
            return range;
        }

        if (foldStyle === "markbegin")
            return;

        var match = line.match(this.foldingStopMarker);
        if (match) {
            var i = match.index + match[0].length;

            if (match[1])
                return this.closingBracketBlock(session, match[1], row, i);

            return session.getCommentFoldRange(row, i, -1);
        }
    };
    
    this.getSectionRange = function(session, row) {
        var line = session.getLine(row);
        var startIndent = line.search(/\S/);
        var startRow = row;
        var startColumn = line.length;
        row = row + 1;
        var endRow = row;
        var maxRow = session.getLength();
        while (++row < maxRow) {
            line = session.getLine(row);
            var indent = line.search(/\S/);
            if (indent === -1)
                continue;
            if  (startIndent > indent)
                break;
            var subRange = this.getFoldWidgetRange(session, "all", row);
            
            if (subRange) {
                if (subRange.start.row <= startRow) {
                    break;
                } else if (subRange.isMultiLine()) {
                    row = subRange.end.row;
                } else if (startIndent == indent) {
                    break;
                }
            }
            endRow = row;
        }
        
        return new Range(startRow, startColumn, endRow, session.getLine(endRow).length);
    };
    this.getCommentRegionBlock = function(session, line, row) {
        var startColumn = line.search(/\s*$/);
        var maxRow = session.getLength();
        var startRow = row;
        
        var re = /^\s*(?:\/\*|\/\/|--)#?(end)?region\b/;
        var depth = 1;
        while (++row < maxRow) {
            line = session.getLine(row);
            var m = re.exec(line);
            if (!m) continue;
            if (m[1]) depth--;
            else depth++;

            if (!depth) break;
        }

        var endRow = row;
        if (endRow > startRow) {
            return new Range(startRow, startColumn, endRow, line.length);
        }
    };

}).call(FoldMode.prototype);

});

ace.define("ace/mode/ion",["require","exports","module","ace/lib/oop","ace/mode/text","ace/mode/ion_highlight_rules","ace/mode/matching_brace_outdent","ace/mode/behaviour/cstyle","ace/mode/folding/cstyle"], function(require, exports, module) {
    "use strict";

    var oop = require("../lib/oop");
    var TextMode = require("./text").Mode;
    var HighlightRules = require("./ion_highlight_rules").IonHighlightRules;
    var MatchingBraceOutdent = require("./matching_brace_outdent").MatchingBraceOutdent;
    var CstyleBehaviour = require("./behaviour/cstyle").CstyleBehaviour;
    var CStyleFoldMode = require("./folding/cstyle").FoldMode;

    var Mode = function() {
        this.HighlightRules = HighlightRules;
        this.$outdent = new MatchingBraceOutdent();
        this.$behaviour = new CstyleBehaviour();
        this.foldingRules = new CStyleFoldMode();
    };
    oop.inherits(Mode, TextMode);

    (function() {

        this.lineCommentStart = "//";
        this.blockComment = {start: "/*", end: "*/"};

        this.getNextLineIndent = function(state, line, tab) {
            var indent = this.$getIndent(line);

            if (state == "start") {
                var match = line.match(/^.*[\{\(\[]\s*$/);
                if (match) {
                    indent += tab;
                }
            }

            return indent;
        };

        this.checkOutdent = function(state, line, input) {
            return this.$outdent.checkOutdent(line, input);
        };

        this.autoOutdent = function(state, doc, row) {
            this.$outdent.autoOutdent(doc, row);
        };

        this.$id = "ace/mode/ion";
    }).call(Mode.prototype);

    exports.Mode = Mode;
});                (function() {
                    ace.require(["ace/mode/ion"], function(m) {
                        if (typeof module == "object" && typeof exports == "object" && module) {
                            module.exports = m;
                        }
                    });
                })();
            