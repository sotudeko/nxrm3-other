import groovy.json.JsonSlurper

class NXRM3Components {
   static void main(String[] args) {
      def fileName = args[0]
      println('reading file: ' + fileName)

      def jsonSlurper = new JsonSlurper()
      def reader = new BufferedReader(new InputStreamReader(new FileInputStream(fileName),"UTF-8"))

      def data = jsonSlurper.parse(reader)

      data.items.each { println it.id }

      def continueToken = data.continuationToken

      if (continueToken != null){
        println data.continuationToken
      }
   }
}



