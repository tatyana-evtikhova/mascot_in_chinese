lesson = {
    'id': 3,
    'title': 'Family Members',
    'icon': '👨‍👩‍👦‍👦',  # Using emoji as icon until we have a custom one
    'content': {
        'stages': [
            {
                'name': 'Family Members',
                'type': 'learning',
                'icon': '👨‍👩‍👦‍👦',
                'subtitle': 'Learn essential family terms in Mandarin',
                'content': '''
                    <div class="learning-section">
                        <div class="section-intro">
                            <p>Learning family terms in Chinese is essential for daily communication and understanding relationships. 
                            Chinese has specific terms for different family members based on age, gender, and whether they are from 
                            the maternal or paternal side of the family.</p>
                        </div>

                        <!-- Immediate Family -->
                        <div class="main-expression" onclick="speakText('爸爸')">
                            <div class="expression-content">
                                <div class="chinese-text">爸爸</div>
                                <div class="expression-details">
                                    <div class="pinyin">bàba</div>
                                    <div class="meaning">father/dad</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('妈妈')">
                            <div class="expression-content">
                                <div class="chinese-text">妈妈</div>
                                <div class="expression-details">
                                    <div class="pinyin">māma</div>
                                    <div class="meaning">mother/mom</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('儿子')">
                            <div class="expression-content">
                                <div class="chinese-text">儿子</div>
                                <div class="expression-details">
                                    <div class="pinyin">érzi</div>
                                    <div class="meaning">son</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('女儿')">
                            <div class="expression-content">
                                <div class="chinese-text">女儿</div>
                                <div class="expression-details">
                                    <div class="pinyin">nǚ'ér</div>
                                    <div class="meaning">daughter</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('老婆')">
                            <div class="expression-content">
                                <div class="chinese-text">老婆</div>
                                <div class="expression-details">
                                    <div class="pinyin">lǎopo</div>
                                    <div class="meaning">wife (informal)</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('老公')">
                            <div class="expression-content">
                                <div class="chinese-text">老公</div>
                                <div class="expression-details">
                                    <div class="pinyin">lǎogōng</div>
                                    <div class="meaning">husband (informal)</div>
                                </div>
                            </div>
                        </div>

                        <!-- Important Notes -->
                        <div class="tone-rule">
                            <div class="rule-header">
                                <span class="rule-icon">💡</span>
                                <span class="rule-title">Important Notes</span>
                            </div>
                            <ul class="usage-notes">
                                <li>Family terms are often repeated (妈妈, 爸爸) for clarity and respect</li>
                                <li>Use 的 to show possession: 我的妈妈 (my mom)</li>
                                <li>Some terms have formal and informal versions</li>
                                <li>Always use the full form when addressing family members</li>
                            </ul>
                        </div>
                    </div>
                '''
            },
            {
                'name': 'Common Usage',
                'type': 'examples',
                'content': '''
                    <div class="usage-examples">
                        
                        <div class="usage-item" onclick="speakText('我爸爸在工作')">
                            <div class="usage-chinese">我爸爸在工作</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">wǒ bàba zài gōngzuò</div>
                                <div class="usage-meaning">My dad is working</div>
                            </div>
                        </div>

                        <div class="usage-item" onclick="speakText('我妈妈在家')">
                            <div class="usage-chinese">我妈妈在家</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">wǒ māma zài jiā</div>
                                <div class="usage-meaning">My mom is at home</div>
                            </div>
                        </div>

                        <div class="usage-item" onclick="speakText('她是我的女儿')">
                            <div class="usage-chinese">她是我的女儿</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">tā shì wǒ de nǚ'ér</div>
                                <div class="usage-meaning">She is my daughter</div>
                            </div>
                        </div>

                        <div class="usage-item" onclick="speakText('我老公在上班')">
                            <div class="usage-chinese">我老公在上班</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">wǒ lǎogōng zài shàngbān</div>
                                <div class="usage-meaning">My husband is at work</div>
                            </div>
                        </div>
                    </div>
                '''
            }
        ],
        'tips': '''
            <div class="study-tips">
                <div class="section-title">
                    <div class="title-with-icon">
                        <span class="icon">💡</span>
                        <span>Study Tips</span>
                    </div>
                </div>
                <div class="tip-block">
                    <h4>Basic Structure</h4>
                    <p>Learn the pattern: 我的[family member] - My [family member]</p>
                </div>

                <div class="tip-block">
                    <h4>Respect Forms</h4>
                    <p>Use full forms (爸爸 instead of 爸) to show respect</p>
                </div>

                <div class="tip-block">
                    <h4>Common Patterns</h4>
                    <p>Practice with: 这是我的[family member] - This is my [family member]</p>
                </div>

                <div class="tip-block">
                    <h4>Daily Usage</h4>
                    <p>Use these terms both for addressing and referring to family members</p>
                </div>
            </div>
        ''',
        'mistakes': '''
            <div class="study-tips warning">
                <div class="tip-block">
                    <h4>Common Mistakes to Avoid</h4>
                    <p>Don't use shortened forms (爸 instead of 爸爸) when addressing family members</p>
                </div>

                <div class="tip-block">
                    <h4>Possession Markers</h4>
                    <p>Don't forget to use 的 when showing possession</p>
                </div>

                <div class="tip-block">
                    <h4>Formality Levels</h4>
                    <p>Be careful with formal vs informal terms in different situations</p>
                </div>

                <div class="tip-block">
                    <h4>Pronunciation</h4>
                    <p>Pay attention to the tones, as they can change meaning</p>
                </div>
            </div>
        '''
    }
} 