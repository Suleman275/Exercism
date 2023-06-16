class SqueakyClean {
    static String clean(String identifier) {
        var s = new StringBuilder();
        var dashFlag = false;

        for(int i = 0; i < identifier.length(); i++){
            char c = identifier.charAt(i);

            if(c ==' '){
                s.append('_');
            }
            else if(Character.isISOControl(c)){
                s.append("CTRL");
            }
            else if(c == '-'){
                dashFlag = true;
            }
            else if (Character.isLetter(c) && (c < 'α' || c >  'ω')) {
                if (dashFlag) {
                    c = Character.toUpperCase(c);
                    dashFlag = false;
                }
                s.append(c);
            }
        }

        return s.toString();
    }
}
