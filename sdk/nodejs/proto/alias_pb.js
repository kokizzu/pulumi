// source: pulumi/alias.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {missingRequire} reports error on implicit type usages.
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!
/* eslint-disable */
// @ts-nocheck

var jspb = require('google-protobuf');
var goog = jspb;
var proto = { pulumirpc: { codegen: { }, testing: { } } }, global = proto;

goog.exportSymbol('proto.pulumirpc.Alias', null, global);
goog.exportSymbol('proto.pulumirpc.Alias.AliasCase', null, global);
goog.exportSymbol('proto.pulumirpc.Alias.Spec', null, global);
goog.exportSymbol('proto.pulumirpc.Alias.Spec.ParentCase', null, global);
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.pulumirpc.Alias = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, proto.pulumirpc.Alias.oneofGroups_);
};
goog.inherits(proto.pulumirpc.Alias, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.pulumirpc.Alias.displayName = 'proto.pulumirpc.Alias';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.pulumirpc.Alias.Spec = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, proto.pulumirpc.Alias.Spec.oneofGroups_);
};
goog.inherits(proto.pulumirpc.Alias.Spec, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.pulumirpc.Alias.Spec.displayName = 'proto.pulumirpc.Alias.Spec';
}

/**
 * Oneof group definitions for this message. Each group defines the field
 * numbers belonging to that group. When of these fields' value is set, all
 * other fields in the group are cleared. During deserialization, if multiple
 * fields are encountered for a group, only the last value seen will be kept.
 * @private {!Array<!Array<number>>}
 * @const
 */
proto.pulumirpc.Alias.oneofGroups_ = [[1,2]];

/**
 * @enum {number}
 */
proto.pulumirpc.Alias.AliasCase = {
  ALIAS_NOT_SET: 0,
  URN: 1,
  SPEC: 2
};

/**
 * @return {proto.pulumirpc.Alias.AliasCase}
 */
proto.pulumirpc.Alias.prototype.getAliasCase = function() {
  return /** @type {proto.pulumirpc.Alias.AliasCase} */(jspb.Message.computeOneofCase(this, proto.pulumirpc.Alias.oneofGroups_[0]));
};



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.pulumirpc.Alias.prototype.toObject = function(opt_includeInstance) {
  return proto.pulumirpc.Alias.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.pulumirpc.Alias} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.pulumirpc.Alias.toObject = function(includeInstance, msg) {
  var f, obj = {
    urn: jspb.Message.getFieldWithDefault(msg, 1, ""),
    spec: (f = msg.getSpec()) && proto.pulumirpc.Alias.Spec.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.pulumirpc.Alias}
 */
proto.pulumirpc.Alias.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.pulumirpc.Alias;
  return proto.pulumirpc.Alias.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.pulumirpc.Alias} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.pulumirpc.Alias}
 */
proto.pulumirpc.Alias.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setUrn(value);
      break;
    case 2:
      var value = new proto.pulumirpc.Alias.Spec;
      reader.readMessage(value,proto.pulumirpc.Alias.Spec.deserializeBinaryFromReader);
      msg.setSpec(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.pulumirpc.Alias.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.pulumirpc.Alias.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.pulumirpc.Alias} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.pulumirpc.Alias.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = /** @type {string} */ (jspb.Message.getField(message, 1));
  if (f != null) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getSpec();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      proto.pulumirpc.Alias.Spec.serializeBinaryToWriter
    );
  }
};



/**
 * Oneof group definitions for this message. Each group defines the field
 * numbers belonging to that group. When of these fields' value is set, all
 * other fields in the group are cleared. During deserialization, if multiple
 * fields are encountered for a group, only the last value seen will be kept.
 * @private {!Array<!Array<number>>}
 * @const
 */
proto.pulumirpc.Alias.Spec.oneofGroups_ = [[5,6]];

/**
 * @enum {number}
 */
proto.pulumirpc.Alias.Spec.ParentCase = {
  PARENT_NOT_SET: 0,
  PARENTURN: 5,
  NOPARENT: 6
};

/**
 * @return {proto.pulumirpc.Alias.Spec.ParentCase}
 */
proto.pulumirpc.Alias.Spec.prototype.getParentCase = function() {
  return /** @type {proto.pulumirpc.Alias.Spec.ParentCase} */(jspb.Message.computeOneofCase(this, proto.pulumirpc.Alias.Spec.oneofGroups_[0]));
};



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.pulumirpc.Alias.Spec.prototype.toObject = function(opt_includeInstance) {
  return proto.pulumirpc.Alias.Spec.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.pulumirpc.Alias.Spec} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.pulumirpc.Alias.Spec.toObject = function(includeInstance, msg) {
  var f, obj = {
    name: jspb.Message.getFieldWithDefault(msg, 1, ""),
    type: jspb.Message.getFieldWithDefault(msg, 2, ""),
    stack: jspb.Message.getFieldWithDefault(msg, 3, ""),
    project: jspb.Message.getFieldWithDefault(msg, 4, ""),
    parenturn: jspb.Message.getFieldWithDefault(msg, 5, ""),
    noparent: jspb.Message.getBooleanFieldWithDefault(msg, 6, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.pulumirpc.Alias.Spec}
 */
proto.pulumirpc.Alias.Spec.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.pulumirpc.Alias.Spec;
  return proto.pulumirpc.Alias.Spec.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.pulumirpc.Alias.Spec} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.pulumirpc.Alias.Spec}
 */
proto.pulumirpc.Alias.Spec.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setName(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setType(value);
      break;
    case 3:
      var value = /** @type {string} */ (reader.readString());
      msg.setStack(value);
      break;
    case 4:
      var value = /** @type {string} */ (reader.readString());
      msg.setProject(value);
      break;
    case 5:
      var value = /** @type {string} */ (reader.readString());
      msg.setParenturn(value);
      break;
    case 6:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setNoparent(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.pulumirpc.Alias.Spec.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.pulumirpc.Alias.Spec.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.pulumirpc.Alias.Spec} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.pulumirpc.Alias.Spec.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getName();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getType();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
  f = message.getStack();
  if (f.length > 0) {
    writer.writeString(
      3,
      f
    );
  }
  f = message.getProject();
  if (f.length > 0) {
    writer.writeString(
      4,
      f
    );
  }
  f = /** @type {string} */ (jspb.Message.getField(message, 5));
  if (f != null) {
    writer.writeString(
      5,
      f
    );
  }
  f = /** @type {boolean} */ (jspb.Message.getField(message, 6));
  if (f != null) {
    writer.writeBool(
      6,
      f
    );
  }
};


/**
 * optional string name = 1;
 * @return {string}
 */
proto.pulumirpc.Alias.Spec.prototype.getName = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.pulumirpc.Alias.Spec} returns this
 */
proto.pulumirpc.Alias.Spec.prototype.setName = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional string type = 2;
 * @return {string}
 */
proto.pulumirpc.Alias.Spec.prototype.getType = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/**
 * @param {string} value
 * @return {!proto.pulumirpc.Alias.Spec} returns this
 */
proto.pulumirpc.Alias.Spec.prototype.setType = function(value) {
  return jspb.Message.setProto3StringField(this, 2, value);
};


/**
 * optional string stack = 3;
 * @return {string}
 */
proto.pulumirpc.Alias.Spec.prototype.getStack = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 3, ""));
};


/**
 * @param {string} value
 * @return {!proto.pulumirpc.Alias.Spec} returns this
 */
proto.pulumirpc.Alias.Spec.prototype.setStack = function(value) {
  return jspb.Message.setProto3StringField(this, 3, value);
};


/**
 * optional string project = 4;
 * @return {string}
 */
proto.pulumirpc.Alias.Spec.prototype.getProject = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 4, ""));
};


/**
 * @param {string} value
 * @return {!proto.pulumirpc.Alias.Spec} returns this
 */
proto.pulumirpc.Alias.Spec.prototype.setProject = function(value) {
  return jspb.Message.setProto3StringField(this, 4, value);
};


/**
 * optional string parentUrn = 5;
 * @return {string}
 */
proto.pulumirpc.Alias.Spec.prototype.getParenturn = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 5, ""));
};


/**
 * @param {string} value
 * @return {!proto.pulumirpc.Alias.Spec} returns this
 */
proto.pulumirpc.Alias.Spec.prototype.setParenturn = function(value) {
  return jspb.Message.setOneofField(this, 5, proto.pulumirpc.Alias.Spec.oneofGroups_[0], value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.pulumirpc.Alias.Spec} returns this
 */
proto.pulumirpc.Alias.Spec.prototype.clearParenturn = function() {
  return jspb.Message.setOneofField(this, 5, proto.pulumirpc.Alias.Spec.oneofGroups_[0], undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.pulumirpc.Alias.Spec.prototype.hasParenturn = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * optional bool noParent = 6;
 * @return {boolean}
 */
proto.pulumirpc.Alias.Spec.prototype.getNoparent = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 6, false));
};


/**
 * @param {boolean} value
 * @return {!proto.pulumirpc.Alias.Spec} returns this
 */
proto.pulumirpc.Alias.Spec.prototype.setNoparent = function(value) {
  return jspb.Message.setOneofField(this, 6, proto.pulumirpc.Alias.Spec.oneofGroups_[0], value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.pulumirpc.Alias.Spec} returns this
 */
proto.pulumirpc.Alias.Spec.prototype.clearNoparent = function() {
  return jspb.Message.setOneofField(this, 6, proto.pulumirpc.Alias.Spec.oneofGroups_[0], undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.pulumirpc.Alias.Spec.prototype.hasNoparent = function() {
  return jspb.Message.getField(this, 6) != null;
};


/**
 * optional string urn = 1;
 * @return {string}
 */
proto.pulumirpc.Alias.prototype.getUrn = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.pulumirpc.Alias} returns this
 */
proto.pulumirpc.Alias.prototype.setUrn = function(value) {
  return jspb.Message.setOneofField(this, 1, proto.pulumirpc.Alias.oneofGroups_[0], value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.pulumirpc.Alias} returns this
 */
proto.pulumirpc.Alias.prototype.clearUrn = function() {
  return jspb.Message.setOneofField(this, 1, proto.pulumirpc.Alias.oneofGroups_[0], undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.pulumirpc.Alias.prototype.hasUrn = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional Spec spec = 2;
 * @return {?proto.pulumirpc.Alias.Spec}
 */
proto.pulumirpc.Alias.prototype.getSpec = function() {
  return /** @type{?proto.pulumirpc.Alias.Spec} */ (
    jspb.Message.getWrapperField(this, proto.pulumirpc.Alias.Spec, 2));
};


/**
 * @param {?proto.pulumirpc.Alias.Spec|undefined} value
 * @return {!proto.pulumirpc.Alias} returns this
*/
proto.pulumirpc.Alias.prototype.setSpec = function(value) {
  return jspb.Message.setOneofWrapperField(this, 2, proto.pulumirpc.Alias.oneofGroups_[0], value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.pulumirpc.Alias} returns this
 */
proto.pulumirpc.Alias.prototype.clearSpec = function() {
  return this.setSpec(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.pulumirpc.Alias.prototype.hasSpec = function() {
  return jspb.Message.getField(this, 2) != null;
};


goog.object.extend(exports, proto.pulumirpc);
